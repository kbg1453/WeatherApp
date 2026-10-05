from supabase import Client
from typing import Optional, List
from ..models.city import City
from ..repositories.city_repository import (
    insert_city,
    get_city_by_name,
    get_city_by_country,
    get_all_cities,
    update_city_by_id
)

def add_city(supabase: Client, name: str, country: str) -> City:
    """
    Fügt eine neue Stadt hinzu.
    """
    city = City(id=None, name=name, country=country)
    print("add_city_service vor")
    insert_city(supabase, city)
    print("add_city_service nach")
    return city

def find_city_by_name(supabase: Client, name: str):
    """
    Sucht eine Stadt anhand des Namens.
    """
    return get_city_by_name(supabase, name)

def find_cities_by_country(supabase: Client, country: str):
    """
    Sucht alle Städte in einem bestimmten Land.
    """
    return get_city_by_country(supabase, country)

def list_all_cities(supabase: Client) -> List[City]:
    """
    Listet alle Städte auf.
    """
    return get_all_cities(supabase)

def modify_city_by_id(supabase: Client, city_id: int, name: Optional[str] = None, country: Optional[str] = None) -> Optional[City]:
    """
    Aktualisiert eine Stadt anhand der ID.
    """
    update_city_by_id(supabase, city_id, name, country)
    return get_city_by_name(supabase, name)  # Hole die aktualisierte Stadt
