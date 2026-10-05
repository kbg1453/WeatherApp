from fastapi import APIRouter, HTTPException
from typing import List
from ..models.city import City
from ..services.city_service import (
    add_city,
    find_city_by_name,
    find_cities_by_country,
    list_all_cities,
    modify_city_by_id
)
from ..database import Database

router = APIRouter()

@router.post("/cities", response_model=City)
def create_city(name: str , country: str ):
    print("post vor der supabase")
    supabase = Database.get_client()
    print("post nach der supabase")
    city = add_city(supabase, name, country)
    return city

@router.get("/cities/{name}", response_model=City)
def get_city_by_name_route(name: str):
    supabase = Database.get_client()
    city = find_city_by_name(supabase, name)
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@router.get("/cities", response_model=List[City])
def get_all_cities_route():
    supabase = Database.get_client()
    return list_all_cities(supabase)

@router.put("/cities/{city_id}", response_model=City)
def update_city(city_id: int, name: str, country: str):
    supabase = Database.get_client()
    city = modify_city_by_id(supabase, city_id, name, country)
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@router.get("/cities/country/{country}", response_model=List[City])
def get_cities_by_country_route(country: str):
    supabase = Database.get_client()
    cities = find_cities_by_country(supabase, country)
    if not cities:
        raise HTTPException(status_code=404, detail="No cities found for the specified country")
    return cities
