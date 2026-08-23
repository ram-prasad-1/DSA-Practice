# 04. The GIL — what it stops, and how to choose a concurrency model
# Run: python 04_gil_and_choosing.py
# The body lives in main() because of the process pool (see 02_multiprocessing.py)



import sys
import sysconfig
import threading
import time
import zlib
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor



JOBS = [5_000_000] * 4
WAITS = [0.05] * 8
counter = 0


def crunch(n):
    return sum(i * i for i in range(n))


def sleeper(seconds):
    time.sleep(seconds)
    return seconds


def compress(data):
    return len(zlib.compress(data, 6))


def unsafe(n):
    global counter
    for _ in range(n):
        current = counter
        time.sleep(0)
        counter = current + 1


def main():
    global counter

    # the GIL is one lock that lets only ONE thread run Python bytecode at a time
    print("python:", sys.version.split()[0])
    print("free-threaded build (no GIL):", bool(sysconfig.get_config_var("Py_GIL_DISABLED")))
    print("switch interval:", sys.getswitchinterval(), "seconds")



    # CPU-bound + threads: no speedup, because the GIL serialises the bytecode
    start = time.perf_counter()
    [crunch(n) for n in JOBS]
    serial_time = time.perf_counter() - start

    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(crunch, JOBS))
    thread_time = time.perf_counter() - start

    print(f"CPU-bound: serial {serial_time:.2f}s | 4 threads {thread_time:.2f}s")



    # CPU-bound + processes: real parallelism, one GIL per interpreter
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=4) as pool:
        list(pool.map(crunch, JOBS))
    print(f"CPU-bound: 4 processes {time.perf_counter() - start:.2f}s")



    # IO-bound + threads: a big speedup, because a thread RELEASES the GIL
    # while it waits on the OS (sleep, sockets, disk)
    start = time.perf_counter()
    [sleeper(s) for s in WAITS]
    serial_io = time.perf_counter() - start

    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(sleeper, WAITS))
    thread_io = time.perf_counter() - start

    print(f"IO-bound:  serial {serial_io:.2f}s | 8 threads {thread_io:.2f}s")



    # C extensions can release the GIL too, so zlib/numpy/hashlib DO parallelise
    data = b"x" * 4_000_000

    start = time.perf_counter()
    [compress(data) for _ in range(4)]
    serial_c = time.perf_counter() - start

    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(compress, [data] * 4))
    thread_c = time.perf_counter() - start

    print(f"zlib in threads: serial {serial_c:.2f}s | 4 threads {thread_c:.2f}s")



    # what the GIL does NOT give you: atomic operations on your own state
    counter = 0
    threads = [threading.Thread(target=unsafe, args=(200,)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("expected 800, got", counter, "— the GIL is not a lock on YOUR data")



    # 3.13+ ships an optional free-threaded build (PEP 703) with no GIL at all;
    # 3.14 makes it officially supported. Subinterpreters (PEP 734, the
    # concurrent.interpreters module in 3.14) are the other escape hatch —
    # one GIL each, inside a single process.
    try:
        from concurrent import interpreters

        interp = interpreters.create()
        interp.exec("x = 1 + 1")
        print("subinterpreters available:", True, "| id", interp.id)
        interp.close()
    except ImportError:
        print("subinterpreters available: False (needs 3.14+)")



# choosing, in one table:
#
#   workload             best tool                     why
#   -------------------  ----------------------------  --------------------------
#   blocking IO, sync    threads / ThreadPoolExecutor  the GIL is released on wait
#   IO, async all down   asyncio (12-async)            no OS stack per task
#   CPU-bound Python     processes / ProcessPool       one GIL per interpreter
#   CPU-bound in C       threads (numpy, zlib, ...)    the extension frees the GIL
#   thousands of sockets asyncio                       a thread costs ~8 MB of stack
#
# and the ordering rule: measure first and reach for concurrency last —
# a better algorithm beats every row above



if __name__ == "__main__":
    main()



# Practice
# Q1. Re-run the CPU benchmark on a free-threaded build (python3.14t) and compare.
# Q2. Why does the zlib benchmark scale with threads but the pure-Python one not?
# Q3. Pick the right tool: 500 HTTP calls / resizing 500 images / parsing one 2 GB log.
