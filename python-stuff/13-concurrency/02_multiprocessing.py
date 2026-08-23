# 02. multiprocessing — separate interpreters, real parallelism
# Run: python 02_multiprocessing.py
# The whole body lives in main() on purpose: the default start method on
# macOS/Windows is `spawn`, which RE-IMPORTS this module in every child, so
# unguarded top-level code would run again in each process.



import multiprocessing as mp
import os
import time



# targets must be importable module-level functions — they are pickled by name
def worker(name):
    return f"{name} from pid {os.getpid()}"


def crunch(n):
    return sum(i * i for i in range(n))


def slow_double(n):
    time.sleep(0.05)
    return n * 2


def produce(q, n):
    for i in range(n):
        q.put(i * i)
    q.put(None)


def add_to_shared(total, lock):
    for _ in range(1000):
        with lock:
            total.value += 1


counter = 0


def bump():
    global counter
    counter += 1000


def main():
    print("start method:", mp.get_start_method(), "| cpus:", mp.cpu_count())
    print("parent pid:", os.getpid())



    # a Process is the thread API with a separate interpreter behind it
    p = mp.Process(target=print, args=("  hello from a child",))
    p.start()
    p.join()
    print("exitcode:", p.exitcode)



    # processes do NOT share memory — a global changed in a child is invisible
    p = mp.Process(target=bump)
    p.start()
    p.join()
    print("parent counter is still", counter)



    # so results come back through a Pool, a Queue, or shared ctypes
    with mp.Pool(processes=2) as pool:
        print(pool.map(slow_double, [1, 2, 3, 4]))
        print(pool.apply(worker, ("apply",)))
        print(list(pool.imap_unordered(slow_double, [1, 2, 3])))



    # the parallelism is real: 4 CPU-bound jobs on 4 cores beat doing them serially
    jobs = [5_000_000] * 4

    start = time.perf_counter()
    serial = [crunch(n) for n in jobs]
    serial_time = time.perf_counter() - start

    start = time.perf_counter()
    with mp.Pool(processes=4) as pool:
        parallel = pool.map(crunch, jobs)
    parallel_time = time.perf_counter() - start

    print(f"serial {serial_time:.2f}s vs parallel {parallel_time:.2f}s")
    print("same answers:", serial == parallel)



    # a Queue passes messages between processes (everything is pickled)
    q = mp.Queue()
    p = mp.Process(target=produce, args=(q, 4))
    p.start()
    got = []
    while (item := q.get()) is not None:
        got.append(item)
    p.join()
    print("via queue:", got)



    # shared memory for plain values, with a lock to make += safe
    total = mp.Value("i", 0)
    lock = mp.Lock()
    procs = [mp.Process(target=add_to_shared, args=(total, lock)) for _ in range(4)]
    for pr in procs:
        pr.start()
    for pr in procs:
        pr.join()
    print("shared value:", total.value)



    # what cannot cross a process boundary: lambdas, closures, local classes,
    # open sockets and files — anything unpicklable
    try:
        with mp.Pool(1) as pool:
            pool.map(lambda x: x, [1])
    except Exception as e:
        print(f"{type(e).__name__}: a lambda is not picklable")



    # the cost: each process is a fresh interpreter (tens of ms) and every
    # argument and result is pickled — use it for chunky work, not tiny tasks
    start = time.perf_counter()
    with mp.Pool(4) as pool:
        pool.map(crunch, [1] * 2000)
    print(f"2000 trivial tasks: {time.perf_counter() - start:.2f}s of mostly overhead")



    # prefer concurrent.futures.ProcessPoolExecutor (file 03) for new code —
    # the same processes behind a nicer API



if __name__ == "__main__":
    main()



# Practice
# Q1. Move one print out of main() to the top level and explain the extra output.
# Q2. Chunk those 2000 tiny tasks into 4 batches and re-time it.
# Q3. Why can a thread target be a lambda but a process target cannot?
