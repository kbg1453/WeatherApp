from fastapi import APIRouter, HTTPException
from typing import List, Optional
from ..models.city_weather import CityWeather
from ..services.city_weather_service import (
    add_city_weather,
    find_weather_by_city_id,
    list_all_weather,
    remove_weather_by_id
)
from ..database import Database

router = APIRouter()

@router.post("/weather", response_model=CityWeather)
def create_city_weather(city_id: int, temperature: float, weather_description: str):
    print("post create_city_weather")
    supabase = Database.get_client()
    city_weather = add_city_weather(supabase, city_id, temperature, weather_description)
    return city_weather

@router.get("/weather/{city_id}", response_model=List[CityWeather])
def get_weather_by_city_id_route(city_id: int):
    supabase = Database.get_client()
    city_weather = find_weather_by_city_id(supabase, city_id)
    if city_weather is None:
        raise HTTPException(status_code=404, detail="Weather not found")
    return city_weather

@router.get("/weather", response_model=List[CityWeather])
def get_all_weather_route():
    supabase = Database.get_client()
    return list_all_weather(supabase)

@router.delete("/weather/{weather_id}", response_model=bool)
def delete_weather_route(weather_id: int):
    supabase = Database.get_client()
    success = remove_weather_by_id(supabase, weather_id)
    if not success:
        raise HTTPException(status_code=404, detail="Weather not found")
    return success

'''
@router.get("/weather/city/{city_name}", response_model=List[CityWeather])
def get_weather_by_city_name_route(city_name: str):
    supabase = Database.get_client()
    city_weather = find_weather_by_city_name(supabase, city_name)
    if city_weather is None:
        raise HTTPException(status_code=404, detail="Weather not found")
    return city_weather
'''

'''

@router.get("/weather/country/{country_name}", response_model=List[CityWeather])
def get_weather_by_country_name_route(country_name: str):
    supabase = Database.get_client()
    city_weathers = find_weather_by_country_name(supabase, country_name)
    if not city_weathers:
        raise HTTPException(status_code=404, detail="No weather data found for the specified country")
    return city_weathers
'''
'''
@router.put("/weather/{weather_id}", response_model=CityWeather)
def update_weather_route(weather_id: int, temperature: Optional[float] = None, weather_description: Optional[str] = None):
    supabase = Database.get_client()
    city_weather = modify_weather_by_id(supabase, weather_id, temperature, weather_description)
    if city_weather is None:
        raise HTTPException(status_code=404, detail="Weather not found")
    return city_weather
'''