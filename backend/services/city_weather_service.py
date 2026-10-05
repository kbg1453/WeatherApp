from supabase import Client
from typing import List
from ..models.city_weather import CityWeather
from ..repositories.city_weather_repository import (
    insert_city_weather,
    get_weather_by_city_id,
    get_all_weather,
    delete_weather_by_id
)


def add_city_weather(supabase: Client, city_id: int, temperature: float, weather_description: str) -> CityWeather:
    print("service add_city_weather vor CityWeather")
    city_weather = CityWeather(id=None,city_id=city_id, temperature=temperature, weather_description=weather_description)
    print("service add_city_weather nach CityWeather")
    insert_city_weather(supabase, city_weather)
    return city_weather

def list_all_weather(supabase: Client) -> List[CityWeather]:
    return get_all_weather(supabase)
def remove_weather_by_id(supabase: Client, weather_id: int) -> bool:
    return delete_weather_by_id(supabase, weather_id)

def find_weather_by_city_id(supabase: Client, city_id: int) -> List[CityWeather]:
    return get_weather_by_city_id(supabase, city_id)

'''

def find_weather_by_city_name(supabase: Client, city_name: str) -> List[CityWeather]:
    return get_weather_by_city_name(supabase, city_name)

def find_weather_by_country_name(supabase: Client, country_name: str) -> List[CityWeather]:
    return get_weather_by_country_name(supabase, country_name)

def modify_weather_by_id(supabase: Client, weather_id: int, temperature: Optional[float] = None, weather_description: Optional[str] = None) -> Optional[CityWeather]:
    update_weather_by_id(supabase, weather_id, temperature, weather_description)
    return get_weather_by_city_id(supabase, weather_id)

'''