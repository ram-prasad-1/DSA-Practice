# 01. async / await — cooperative concurrency on a single thread
# Run: python 01_async_await_basics.py



import asyncio
import inspect
import time



# `async def` defines a coroutine FUNCTION; calling it returns a coroutine object
async def hello():
    return "hi"


coro = hello()
print(type(coro).__name__)
coro.close()
print(asyncio.run(hello()))



# nothing runs until it is awaited or scheduled — dropping one without awaiting
# prints "RuntimeWarning: coroutine was never awaited"
async def main():
    return await hello()


print(asyncio.run(main()))



# await hands control back to the event loop while it waits
async def slow(name, seconds):
    print(f"  {name} start")
    await asyncio.sleep(seconds)
    print(f"  {name} done")
    return name


async def sequential():
    start = time.perf_counter()
    a = await slow("a", 0.1)
    b = await slow("b", 0.1)
    return a, b, round(time.perf_counter() - start, 2)


print(asyncio.run(sequential()))



# awaiting one after another is just slow synchronous code with extra steps —
# concurrency needs the awaitables scheduled TOGETHER
async def concurrent():
    start = time.perf_counter()
    a, b = await asyncio.gather(slow("a", 0.1), slow("b", 0.1))
    return a, b, round(time.perf_counter() - start, 2)


print(asyncio.run(concurrent()))



# asyncio.run creates a loop, runs the coroutine, closes the loop — one per program
print(asyncio.run(hello()))
try:
    asyncio.get_running_loop()
except RuntimeError as e:
    print("RuntimeError:", e)



# you cannot await outside a coroutine, and you should not call run() inside one
async def nested():
    inner = hello()
    try:
        asyncio.run(inner)
    except RuntimeError as e:
        return f"RuntimeError: {e}"
    finally:
        inner.close()


print(asyncio.run(nested()))



# await only works on awaitables: coroutines, Tasks and Futures
async def check():
    pending = hello()
    print(asyncio.iscoroutine(pending), inspect.iscoroutinefunction(hello))
    pending.close()
    fut = asyncio.get_running_loop().create_future()
    fut.set_result(42)
    return await fut


print(asyncio.run(check()))



# sleep(0) is the explicit "let other tasks run" yield point
async def yielding(name, n):
    for i in range(n):
        print(f"  {name}{i}", end=" ")
        await asyncio.sleep(0)


async def interleave():
    await asyncio.gather(yielding("a", 3), yielding("b", 3))
    print()


asyncio.run(interleave())



# async is for IO-bound waiting (network, disk, subprocesses).
# It gives you concurrency, NOT parallelism — one thread, one core.



# Practice
# Q1. Write fetch(url) that sleeps a random time and returns the url, then run 5 concurrently.
# Q2. What warning do you get if you call a coroutine function and never await it?
# Q3. Why does sequential() take ~0.2s but concurrent() ~0.1s?
