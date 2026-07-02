import asyncio
import time

from app.api_client import fetch_weather
from app.cities import CITIES

from app.database import (
    create_pool,
    insert_weather
)


async def main():

    start = time.perf_counter()

    pool = await create_pool()

    tasks = [
        fetch_weather(city, lat, lon)
        for city, lat, lon in CITIES
    ]

    results = await asyncio.gather(
    *tasks,
    return_exceptions=True
)

for result in results:

    if isinstance(result, Exception):
        print(f"FAILED: {result}")
        continue

    print(result)

     await insert_weather(
        pool,
        result
    )

    end = time.perf_counter()

    print(f"\nProcessed {len(results)} cities")
    print(f"Completed in {end - start:.2f} seconds")

    await pool.close()


asyncio.run(main())