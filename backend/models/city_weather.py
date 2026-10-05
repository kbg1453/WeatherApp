# models/city_weather.py
from dataclasses import dataclass

@dataclass
class CityWeather:
    id: int
    city_id: int
    temperature: float
    weather_description: str