import asyncio
from dataclasses import dataclass
from typing import List, Awaitable

@dataclass
class Ticket:
    number: int
    key: str

async def coroutines_execution_order(coros: List[Awaitable[Ticket]]) -> str:
    results = await asyncio.gather(*coros)
    sorted_results = sorted(results, key=lambda ticket: ticket.number)
    result_string = ''.join(ticket.key for ticket in sorted_results)

    return result_string
