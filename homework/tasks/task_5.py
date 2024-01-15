import asyncio
from typing import Coroutine

async def limit_execution_time(coro: Coroutine, max_execution_time: float) -> None:
    try:
        await asyncio.wait_for(coro, max_execution_time)
    except asyncio.TimeoutError:
        print("Корутина превысила максимально допустимое время выполнения.")

async def limit_execution_time_many(*coros: Coroutine, max_execution_time: float) -> None:
    try:
        await asyncio.wait_for(asyncio.gather(*coros), max_execution_time)
    except asyncio.TimeoutError:
        print("Одна или несколько корутин превысили максимально допустимое время выполнения.")
