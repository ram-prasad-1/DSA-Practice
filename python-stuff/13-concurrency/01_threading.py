# 01. threading — concurrent waiting, shared memory, and locks
# Run: python 01_threading.py



import threading
import time



# start() runs the target in a new thread; join() waits for it to finish
def worker(name, seconds):
    time.sleep(seconds)
    print(f"  {name} finished")


t = threading.Thread(target=worker, args=("solo", 0.05))
t.start()
print("  main keeps going, alive =", t.is_alive())
t.join()
print(t.is_alive())



# many threads overlap their WAITING, so the total is the slowest, not the sum
start = time.perf_counter()
threads = [threading.Thread(target=worker, args=(f"t{i}", 0.05)) for i in range(4)]
for th in threads:
    th.start()
for th in threads:
    th.join()
print("elapsed:", round(time.perf_counter() - start, 2))



# threads share memory — which is the whole point and the whole problem
counter = 0


def unsafe_increment(n):
    global counter
    for _ in range(n):
        current = counter
        time.sleep(0)
        counter = current + 1


threads = [threading.Thread(target=unsafe_increment, args=(200,)) for _ in range(4)]
for th in threads:
    th.start()
for th in threads:
    th.join()
print("expected 800, got", counter)



# a Lock makes the read-modify-write atomic
counter = 0
lock = threading.Lock()


def safe_increment(n):
    global counter
    for _ in range(n):
        with lock:
            current = counter
            time.sleep(0)
            counter = current + 1


threads = [threading.Thread(target=safe_increment, args=(200,)) for _ in range(4)]
for th in threads:
    th.start()
for th in threads:
    th.join()
print("expected 800, got", counter)



# a plain Lock is not reentrant — the same thread deadlocks on itself
lock.acquire()
print("same thread acquiring again:", lock.acquire(timeout=0.01))
lock.release()

rlock = threading.RLock()
with rlock:
    with rlock:
        print("RLock is reentrant")



# returning a value: threads do not, so use a queue (or a Future — see file 03)
import queue

results = queue.Queue()


def produce(n):
    results.put(n * n)


threads = [threading.Thread(target=produce, args=(i,)) for i in range(4)]
for th in threads:
    th.start()
for th in threads:
    th.join()
print(sorted(results.queue))



# Event for signalling, Semaphore for limiting concurrency
ready = threading.Event()


def wait_for_signal():
    ready.wait(timeout=1)
    print("  got the signal")


threading.Thread(target=wait_for_signal).start()
time.sleep(0.01)
ready.set()
time.sleep(0.02)

sem = threading.Semaphore(2)
peak = {"now": 0, "max": 0}
plock = threading.Lock()


def limited():
    with sem:
        with plock:
            peak["now"] += 1
            peak["max"] = max(peak["max"], peak["now"])
        time.sleep(0.02)
        with plock:
            peak["now"] -= 1


threads = [threading.Thread(target=limited) for _ in range(6)]
for th in threads:
    th.start()
for th in threads:
    th.join()
print("peak concurrent:", peak["max"])



# daemon threads die with the process; non-daemon threads keep it alive
d = threading.Thread(target=time.sleep, args=(30,), daemon=True)
d.start()
print("daemon:", d.daemon, "| active threads:", threading.active_count())



# thread-local storage gives each thread its own copy of a name
local = threading.local()


def set_and_read(value):
    local.value = value
    time.sleep(0.01)
    print(f"  thread sees {local.value}")


for v in ("a", "b"):
    threading.Thread(target=set_and_read, args=(v,)).start()
time.sleep(0.05)



# threads are for BLOCKING IO. For CPU-bound work see 02 and 04 in this folder.



# Practice
# Q1. Why does unsafe_increment lose updates even though CPython has a GIL?
# Q2. Replace the queue with concurrent.futures and compare the code.
# Q3. Write a producer/consumer pair with queue.Queue and a sentinel to stop.
