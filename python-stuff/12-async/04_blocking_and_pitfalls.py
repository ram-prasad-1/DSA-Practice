# 04. Blocking calls and other async traps
# Run: python 04_blocking_and_pitfalls.py



import asyncio
import time



# a blocking call inside a coroutine freezes the WHOLE event loop
async def blocking(name):
    time.sleep(0.05)
    return name


async def all_blocked():
    start = time.perf_counter()
    await asyncio.gather(blocking("a"), blocking("b"), blocking("c"))
    return round(time.perf_counter() - start, 2)


print("time.sleep in a coroutine:", asyncio.run(all_blocked()))



# await asyncio.sleep instead — now they overlap
async def non_blocking(name):
    await asyncio.sleep(0.05)
    return name


async def all_concurrent():
    start = time.perf_counter()
    await asyncio.gather(non_blocking("a"), non_blocking("b"), non_blocking("c"))
    return round(time.perf_counter() - start, 2)


print("asyncio.sleep:", asyncio.run(all_concurrent()))



# for library code you cannot change, push it onto a thread with to_thread
def legacy_io(name):
    time.sleep(0.05)
    return f"{name} via thread"


async def offloaded():
    start = time.perf_counter()
    results = await asyncio.gather(*(asyncio.to_thread(legacy_io, n) for n in "abc"))
    return results[0], round(time.perf_counter() - start, 2)


print(asyncio.run(offloaded()))



# run_in_executor is the general form; None means the loop's default thread pool
def legacy_cpu(n):
    return sum(i * i for i in range(n))


async def in_executor():
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, legacy_cpu, 100_000)


print("run_in_executor:", asyncio.run(in_executor()))



# CPU-bound work needs a PROCESS pool — threads still fight over the GIL.
# It is not demonstrated here on purpose: a process pool re-imports this module
# in every child, so a flat script would re-run itself.
# See 13-concurrency/03_concurrent_futures.py for the guarded version.



# forgetting await gives you a coroutine object, not a result
async def forgot():
    result = non_blocking("x")
    print("  got a", type(result).__name__, "not a str")
    result.close()
    return await non_blocking("x")


print(asyncio.run(forgot()))



# a synchronous function cannot await — async is "all the way down"
def sync_caller():
    try:
        return asyncio.get_running_loop()
    except RuntimeError:
        return "no loop here; call asyncio.run() at the top level only"


print(sync_caller())



# asyncio.run cannot be nested (see 01) — from inside a coroutine, just await



# a long CPU loop with no await starves every other task
async def greedy(order):
    for _ in range(3):
        sum(i for i in range(200_000))
        order.append("greedy")


async def polite(order):
    for _ in range(3):
        await asyncio.sleep(0)
        order.append("polite")


async def starvation():
    order = []
    await asyncio.gather(greedy(order), polite(order))
    return order


print(asyncio.run(starvation()))



# unbounded concurrency is its own bug — bound it with a Semaphore
async def fetch(sem, state):
    async with sem:
        state["now"] += 1
        state["peak"] = max(state["peak"], state["now"])
        await asyncio.sleep(0.01)
        state["now"] -= 1


async def bounded():
    sem = asyncio.Semaphore(3)
    state = {"now": 0, "peak": 0}
    await asyncio.gather(*(fetch(sem, state) for _ in range(9)))
    return state["peak"]


print("peak in flight:", asyncio.run(bounded()))



# choosing: threads for blocking IO in sync code, asyncio for IO-bound code you
# write async end to end, processes for CPU-bound work. Async is not faster —
# it just stops you paying for idle waiting.



# Practice
# Q1. Time 20 requests.get() calls against 20 asyncio.to_thread wrapped ones.
# Q2. Why does `time.sleep(1)` in one coroutine delay all the others?
# Q3. Find a blocking call hiding in a library you use (hint: DNS, file reads, logging).
