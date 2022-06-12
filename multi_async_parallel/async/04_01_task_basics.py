import time
import asyncio
from multi_async_parallel.asyncio.decorator import async_measure_time


async def tick():
    print('tick')
    await asyncio.sleep(1)
    print('tock')


@async_measure_time
async def main():
    t1 = asyncio.create_task(tick(), name='tick1')
    t2 = asyncio.create_task(tick(), name='tick2')

    # await t1
    # await t2
    await asyncio.gather(t1, t2)

    print(f'Task {t1.get_name()}, Done={t1.done()}')
    print(f'Task {t2.get_name()}, Done={t2.done()}')


if __name__ == '__main__':
    asyncio.run(main())
    # main()
