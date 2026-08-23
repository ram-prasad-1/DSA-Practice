# 03. async for, async with, async generators
# Run: python 03_async_iterators_and_context.py



import asyncio



# an async generator: `async def` plus `yield`, consumed with `async for`
async def ticker(count, delay=0.01):
    for i in range(count):
        await asyncio.sleep(delay)
        yield i


async def consume():
    results = []
    async for value in ticker(3):
        results.append(value)
    return results


print(asyncio.run(consume()))



# async comprehensions work too
async def comprehend():
    return [v * 2 async for v in ticker(3)], {v async for v in ticker(2)}


print(asyncio.run(comprehend()))



# the protocol underneath: __aiter__ / __anext__ raising StopAsyncIteration
class Countdown:
    def __init__(self, start):
        self.n = start

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.n <= 0:
            raise StopAsyncIteration
        await asyncio.sleep(0)
        self.n -= 1
        return self.n + 1


async def use_protocol():
    return [n async for n in Countdown(3)]


print(asyncio.run(use_protocol()))



# an async context manager: __aenter__ / __aexit__, used with `async with`
class Connection:
    def __init__(self, name):
        self.name = name

    async def __aenter__(self):
        await asyncio.sleep(0)
        print(f"  connected to {self.name}")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await asyncio.sleep(0)
        print(f"  closed {self.name}")
        return False

    async def query(self, sql):
        await asyncio.sleep(0.01)
        return f"rows for {sql!r}"


async def use_connection():
    async with Connection("db") as conn:
        return await conn.query("SELECT 1")


print(asyncio.run(use_connection()))



# contextlib.asynccontextmanager is the short form
from contextlib import asynccontextmanager


@asynccontextmanager
async def connection(name):
    print(f"  open {name}")
    try:
        yield name
    finally:
        await asyncio.sleep(0)
        print(f"  close {name}")


async def use_short_form():
    async with connection("cache") as name:
        return f"used {name}"


print(asyncio.run(use_short_form()))



# aclosing guarantees the generator's finally block runs on early exit
from contextlib import aclosing


async def resourceful():
    try:
        yield 1
        yield 2
    finally:
        print("  generator cleanup")


async def early_exit():
    async with aclosing(resourceful()) as gen:
        async for value in gen:
            return f"stopped at {value}"


print(asyncio.run(early_exit()))



# an async queue is the idiomatic producer/consumer channel
async def producer(q, n):
    for i in range(n):
        await q.put(i)
        await asyncio.sleep(0.01)
    await q.put(None)


async def consumer(q, out):
    while (item := await q.get()) is not None:
        out.append(item)


async def pipeline():
    q = asyncio.Queue(maxsize=2)
    out = []
    await asyncio.gather(producer(q, 4), consumer(q, out))
    return out


print(asyncio.run(pipeline()))



# locks and semaphores work the same way, with `async with`
async def limited(sem, name, order):
    async with sem:
        await asyncio.sleep(0.01)
        order.append(name)


async def with_semaphore():
    sem = asyncio.Semaphore(2)
    order = []
    await asyncio.gather(*(limited(sem, n, order) for n in "abcd"))
    return order


print(asyncio.run(with_semaphore()))



# Practice
# Q1. Write an async generator that paginates an API until a page is empty.
# Q2. Why does a Semaphore(2) matter when fetching 500 URLs concurrently?
# Q3. What breaks if you use `with` instead of `async with` on Connection?
