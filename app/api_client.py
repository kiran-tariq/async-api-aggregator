import asyncio
import aiohttp

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    wait_random,
)

from app.models import WeatherResult


# Maximum 10 concurrent API calls
semaphore = asyncio.Semaphore(3)


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(min=1, max=10) + wait_random(0, 1),
    reraise=True,
)
async def fetch_weather(
    city: str,
    latitude: float,
    longitude: float,
) -> WeatherResult:

    async with semaphore:

        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={latitude}"
            f"&longitude={longitude}"
            f"&current=temperature_2m,wind_speed_10m"
        )

        try:
            async with aiohttp.ClientSession() as session:

                async with session.get(url) as response:

                    response.raise_for_status()

                    data = await response.json()

                    return WeatherResult(
                        city=city,
                        temperature=data["current"]["temperature_2m"],
                        windspeed=data["current"]["wind_speed_10m"],
                    )

        except Exception as e:
            print(f"Error fetching {city}: {e}")
            raise