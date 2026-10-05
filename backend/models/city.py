from dataclasses import dataclass
from typing import List, Optional
from .city_weather import CityWeather

@dataclass
class City:
    id: int
    name: str
    country: str
    weather_data: Optional[List[CityWeather]] = None