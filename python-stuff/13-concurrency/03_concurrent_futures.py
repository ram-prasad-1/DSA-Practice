# 03. concurrent.futures — one API for threads and processes
# Run: python 03_concurrent_futures.py
# The body lives in main() because the process pool re-imports this module in
# every child (see 02_multiprocessing.py)



import time
from concurrent.futures import (
    ThreadPoolExecutor,
    ProcessPoolExecutor,
    as_completed,
    wait,
    FIRST_COMPLETED,
)



def fetch(name, seconds=0.05):
    time.sleep(seconds)
    return f"{name} fetched"


def crunch(n):
    return sum(i * i for i in range(n))


def flaky(n):
    if n == 2:
        raise ValueError("cannot handle 2")
    return n * 10


def run_with(executor_cls, workers=2):
    with executor_cls(max_workers=workers) as pool:
        return list(pool.map(fetch, ["a", "b"]))


def main():
    # submit returns a Future — a handle on a result that is not ready yet
    with ThreadPoolExecutor(max_workers=4) as pool:
        future = pool.submit(fetch, "one")
        print("done yet?", future.done())
        print(future.result(), future.done())



    # map keeps input order and is the shortest form for the simple case
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as pool:
        print(list(pool.map(fetch, ["a", "b", "c", "d"])))
    print("elapsed:", round(time.perf_counter() - start, 2))



    # as_completed yields futures in COMPLETION order
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {
            pool.submit(fetch, n, s): n
            for n, s in [("slow", 0.06), ("mid", 0.03), ("fast", 0.01)]
        }
        for fut in as_completed(futures):
            print("  finished:", futures[fut], "->", fut.result())



    # an exception is stored in the Future and re-raised at .result()
    with ThreadPoolExecutor() as pool:
        futures = [pool.submit(flaky, n) for n in (1, 2, 3)]
        for fut in futures:
            try:
                print("  ok:", fut.result())
            except ValueError as e:
                print(f"  ValueError: {e}")
        print("exception object:", type(futures[1].exception()).__name__)



    # with map(), it surfaces while you ITERATE and stops the iteration there
    with ThreadPoolExecutor() as pool:
        try:
            print(list(pool.map(flaky, (1, 2, 3))))
        except ValueError as e:
            print("map raised:", e)



    # wait() gives you control over how long to block
    with ThreadPoolExecutor(max_workers=3) as pool:
        futures = [pool.submit(fetch, f"t{i}", 0.01 * (i + 1)) for i in range(3)]
        done, not_done = wait(futures, return_when=FIRST_COMPLETED)
        print(f"{len(done)} done, {len(not_done)} still running")



    # timeouts, cancellation and callbacks
    with ThreadPoolExecutor(max_workers=1) as pool:
        slow = pool.submit(fetch, "slow", 0.2)
        queued = pool.submit(fetch, "queued")
        print("cancelled the queued one:", queued.cancel())
        try:
            slow.result(timeout=0.01)
        except TimeoutError:
            print("TimeoutError: still running")
        slow.add_done_callback(lambda f: print("  callback:", f.result()))



    # the executor shuts down and waits when the with block exits;
    # shutdown(wait=False, cancel_futures=True) is the impatient version
    pool = ThreadPoolExecutor(max_workers=1)
    pool.submit(fetch, "x", 0.01)
    pool.shutdown(wait=True)
    try:
        pool.submit(fetch, "y")
    except RuntimeError as e:
        print("RuntimeError:", e)



    # ProcessPoolExecutor is the SAME API with real parallelism behind it
    jobs = [5_000_000] * 4

    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as pool:
        threaded = list(pool.map(crunch, jobs))
    threaded_time = time.perf_counter() - start

    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=4) as pool:
        processed = list(pool.map(crunch, jobs))
    process_time = time.perf_counter() - start

    print(f"CPU-bound in threads {threaded_time:.2f}s vs processes {process_time:.2f}s")
    print("same answers:", threaded == processed)



    # chunksize batches items per worker — it matters a lot for many small tasks
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=4) as pool:
        list(pool.map(crunch, [1000] * 4000, chunksize=1))
    one = time.perf_counter() - start

    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=4) as pool:
        list(pool.map(crunch, [1000] * 4000, chunksize=500))
    many = time.perf_counter() - start

    print(f"chunksize=1 {one:.2f}s vs chunksize=500 {many:.2f}s")



    # swapping ThreadPoolExecutor for ProcessPoolExecutor is a one-word change —
    # which is exactly why this is the API to reach for first
    print(run_with(ThreadPoolExecutor))
    print(run_with(ProcessPoolExecutor))



if __name__ == "__main__":
    main()



# Practice
# Q1. Fetch 20 URLs with a ThreadPoolExecutor and collect failures separately.
# Q2. Why does the threaded CPU benchmark above show no speedup?
# Q3. When is submit + as_completed better than map?
