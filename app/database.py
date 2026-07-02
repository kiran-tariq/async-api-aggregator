import asyncpg
from app.config import DATABASE_URL


async def create_pool():
    """
    Create PostgreSQL connection pool.
    """
    return await asyncpg.create_pool(
        DATABASE_URL,
        min_size=1,
        max_size=10
    )


async def insert_weather(pool, weather):
    """
    Insert one weather record into database.
    """

    async with pool.acquire() as conn:

        print(f"Inserting: {weather.city}")

        await conn.execute(
            """
            INSERT INTO weather_results
            (city, temperature, windspeed)
            VALUES ($1, $2, $3)
            """,
            weather.city,
            weather.temperature,
            weather.windspeed
        )


async def count_rows(pool):
    """
    Count total rows in weather_results table.
    """

    async with pool.acquire() as conn:

        return await conn.fetchval(
            """
            SELECT COUNT(*)
            FROM weather_results
            """
        )


async def get_all_weather(pool):
    """
    Fetch all weather records.
    """

    async with pool.acquire() as conn:

        return await conn.fetch(
            """
            SELECT *
            FROM weather_results
            ORDER BY created_at DESC
            """
        )