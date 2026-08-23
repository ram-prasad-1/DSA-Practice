# 02. Tasks, gather, TaskGroup, timeouts and cancellation
# Run: python 02_tasks_and_gather.py



import asyncio
import time



async def work(name, seconds, fail=False):
    await asyncio.sleep(seconds)
    if fail:
        raise ValueError(f"{name} failed")
    return f"{name} done"



# create_task schedules a coroutine to run in the background NOW
async def with_tasks():
    task = asyncio.create_task(work("bg", 0.05))
    print("  task created, not awaited yet:", task.done())
    await asyncio.sleep(0)
    result = await task
    return result, task.done()


print(asyncio.run(with_tasks()))



# gather runs many awaitables concurrently and returns results IN ORDER
async def gathered():
    start = time.perf_counter()
    results = await asyncio.gather(work("a", 0.1), work("b", 0.05), work("c", 0.02))
    return results, round(time.perf_counter() - start, 2)


print(asyncio.run(gathered()))



# by default gather cancels nothing and propagates the FIRST exception
async def gather_raises():
    try:
        await asyncio.gather(work("a", 0.05), work("b", 0.01, fail=True))
    except ValueError as e:
        return f"ValueError: {e}"


print(asyncio.run(gather_raises()))



# return_exceptions=True collects them instead of raising
async def gather_collects():
    results = await asyncio.gather(
        work("a", 0.01), work("b", 0.01, fail=True), return_exceptions=True
    )
    return [r if not isinstance(r, Exception) else f"<{type(r).__name__}>" for r in results]


print(asyncio.run(gather_collects()))



# TaskGroup (3.11+) is the modern default: if one task fails, the rest are
# CANCELLED and the errors arrive together as an ExceptionGroup
# (note: `return` is not allowed inside an except* block — assign, then return)
async def with_taskgroup():
    summary = "no error"
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(work("a", 0.2))
            tg.create_task(work("b", 0.01, fail=True))
    except* ValueError as eg:
        summary = f"ExceptionGroup with {len(eg.exceptions)}: {eg.exceptions[0]}"
    return summary


print(asyncio.run(with_taskgroup()))



# a TaskGroup also waits for everything before leaving the block
async def taskgroup_results():
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(work(n, 0.01)) for n in "abc"]
    return [t.result() for t in tasks]


print(asyncio.run(taskgroup_results()))



# as_completed yields results in COMPLETION order
async def in_completion_order():
    coros = [work("slow", 0.06), work("mid", 0.03), work("fast", 0.01)]
    return [await done for done in asyncio.as_completed(coros)]


print(asyncio.run(in_completion_order()))



# timeouts: asyncio.timeout (3.11+) as a context manager, or wait_for
async def with_timeout():
    try:
        async with asyncio.timeout(0.02):
            await work("slow", 0.5)
    except TimeoutError:
        return "timed out (timeout)"


async def with_wait_for():
    try:
        await asyncio.wait_for(work("slow", 0.5), timeout=0.02)
    except TimeoutError:
        return "timed out (wait_for)"


print(asyncio.run(with_timeout()), "|", asyncio.run(with_wait_for()))



# cancellation is delivered as CancelledError inside the task — clean up, re-raise
async def cancellable():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("  cleaning up before cancellation")
        raise


async def cancel_it():
    task = asyncio.create_task(cancellable())
    await asyncio.sleep(0.01)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        return "cancelled", task.cancelled()


print(asyncio.run(cancel_it()))



# never swallow CancelledError, and never let a task's exception go unretrieved
async def orphan():
    task = asyncio.create_task(work("orphan", 0.01, fail=True))
    await asyncio.sleep(0.05)
    print("  task exception was:", type(task.exception()).__name__)


asyncio.run(orphan())



# keep a reference to background tasks — the loop only holds a weak one
async def keep_refs():
    background = set()
    for n in "ab":
        t = asyncio.create_task(work(n, 0.01))
        background.add(t)
        t.add_done_callback(background.discard)
    await asyncio.sleep(0.05)
    return len(background)


print(asyncio.run(keep_refs()))



# Practice
# Q1. Convert gather_collects() to a TaskGroup and note the behaviour change.
# Q2. Wrap 3 tasks in asyncio.timeout(0.05) so a slow one cancels the others.
# Q3. Why must a task hold a strong reference somewhere?
