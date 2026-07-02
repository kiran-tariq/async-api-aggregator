from pydantic import BaseModel


class WeatherResult(BaseModel):
    city: str
    temperature: float
    windspeed: float