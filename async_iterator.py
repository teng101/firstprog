import asyncio

#waits for 1 second between each yield using the asyncio.sleep() function
async def async_generator():
    yield 1
    await asyncio.sleep(1)
    yield 2
    await asyncio.sleep(1)
    yield 3

async def main():
    async for value in async_generator():
        print(value)
"""
#function is defined as an async function that awaits the main() coroutine
async def run_main():
    await main()"""

"""
#For python earlier than 3.7
loop = asyncio.get_event_loop()
loop.run_until_complete(run_main())"""

#used to run the run_main() coroutine
asyncio.run(main())

####################################################

#iterator to count odd numbers

class EvenCounter:

    def __init__(self, end_range):
        self.end = end_range
        self.start = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.start < self.end-1:
            self.start += 2
            return self.start
        else:
            raise StopAsyncIteration


async def main():
    async for c in EvenCounter(10):
        print(c)

asyncio.run(main())