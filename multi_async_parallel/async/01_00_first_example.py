# import time
#
# from multi_async_parallel.asyncio.decorator import measure_time
#
#
# def tick():
#     print('tick')
#     time.sleep(1)
#     print('tock')
#
#
# @measure_time
# def main():
#     for _ in range(3):
#         tick()
#
#
# if __name__ == '__main__':
#     main()

"""Async"""

import time
import asyncio
from .decorator import async_measure_time


async def tick():
    print('tick')
    await asyncio.sleep(1)
    print('tock')


@async_measure_time
async def main():
    # for _ in range(3):
    #     tick()
    await asyncio.gather(tick(), tick(), tick())


if __name__ == '__main__':
    asyncio.run(main())
    # main()
