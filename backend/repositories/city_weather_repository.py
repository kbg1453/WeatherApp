from supabase import Client
from typing import Optional, List
from ..models.city_weather import CityWeather

def insert_city_weather(supabase: Client, city_weather: CityWeather):
    """
    Fügt einen neuen CityWeather-Datensatz hinzu.
    """
    print("insert_city_weather",)
    response = supabase.table("city_weather").insert({
        "city_id": city_weather.city_id,
        "temperature": city_weather.temperature,
        "weather_description": city_weather.weather_description.strip()
    }).execute()
    return response.data[0]

def get_weather_by_city_id(supabase: Client, city_id: int) -> List[CityWeather]:
    """
    Holt das Wetter für eine bestimmte Stadt anhand der Stadt-ID.
    """
    print("get_weather_by_city_id")
    response = supabase.table("city_weather").select("*").eq("city_id", city_id).execute()
    #data = response.data
    return response.data
   # if data:
   #     return data
   # return None

def get_all_weather(supabase: Client) -> List[CityWeather]:
    """
    Holt alle CityWeather-Datensätze.
    """
    print("get_all_weather")
    response = supabase.table("city_weather").select("*").order("id").execute()
    #return [CityWeather(**record) for record in response.data]
    return response.data

def delete_weather_by_id(supabase: Client, weather_id: int) -> bool:
    """
    Löscht einen CityWeather-Datensatz anhand der ID.
    """
    response = supabase.table("city_weather").delete().eq("id", weather_id).execute()
    return response.data is not None


# in der bearbeitung
def get_weather_by_city_name(supabase: Client, city_name: str) -> List[CityWeather]:
    """
    Holt das Wetter für eine bestimmte Stadt anhand des Stadtnamens mit einem Join.
    """
    # Verwende eine SQL-ähnliche Abfrage, um die Tabellen zu joinen
    query = (
        f"SELECT cw.* FROM city_weather as cw "
        f"JOIN cities  as c ON cw.city_id = c.id "
        f"WHERE c.name = '{city_name.strip()}'"
    )
    print("get_weather_by_city_name ",query)
   # response = supabase.sql(query).execute()
     # (f"SELECT cw.* FROM city_weather as cw ")
    #response= ("city_weather as cw  JOIN cities  as c ON cw.city_id = c.id").select("*").eq("c.name = '{city_name.strip()}'").execute()
   # data = response.data
    
    response = supabase.table("city_weather").select("""
       *,
        cities(*)
        """).execute()
    print("get_weather_by_city_name response ",response)
    
    return response.data
# in der bearbeitung
def get_weather_by_country_name(supabase: Client, country_name: str) -> List[CityWeather]:
    """
    Holt das Wetter für alle Städte in einem bestimmten Land anhand des Ländernamens mit einem Join.
    """
    # Verwende eine SQL-ähnliche Abfrage, um die Tabellen zu joinen
    query = (
         f"SELECT cw.* FROM city_weather as cw "
         f"JOIN cities  as c ON cw.city_id = c.id "
         f"WHERE c.country = '{country_name.strip()}'"
    )
    
    response = supabase.sql(query).execute()
    data = response.data
    
    if data:
        return data
    return None


