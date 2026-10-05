from supabase import Client
from typing import  Optional
from ..models.city import City
from postgrest.exceptions import APIError
import logging 

logger = logging.getLogger() # Root

#wird stadt in der Datenbank gespeichert.
def insert_city(supabase: Client, city: City):
    try:
        logger.info("request Supebase: insert City")
        response = supabase.table("cities").insert({
            "name": city.name.strip(),
            "country": city.country.strip()
        }).execute()
    
        data = response.data[0]        
        if data:
            # Erfolgreich eingefügt           
            logger.info("Stadt erfolgreich hinzugefügt")
            return data
        else:
            logger.warning("Stadt könnte nicht erfolgreich hinzugefügt")
            return None

    except APIError as e:
        # Fängt Supabase-spezifische Fehler ab (z. B. Duplikate, fehlende Tabellen)        
        logger.critical(f"Supabase API-Fehler ({e.code}): {e.message}")
        return None
    except Exception as e:
        # Fängt alle anderen unerwarteten Fehler ab (z. B. Netzwerkprobleme)
        logger.critical(f"Unerwarteter Fehler: {e}")
        return None

# Logik, um die Stadte durch ihrer Name aus der Datenbank abzurufen
def get_city_by_name(supabase: Client, name: str) :
    
    try:
        logger.info("request Supebase: get_city_by_name")
        name = name.strip()
        response = supabase.table("cities").select("*").eq("name", name).execute()
        data = response.data[0]        
        if data:
            # Erfolgreich abgeholt
            logger.info("Stadt erfolgreich aus der Datenbank abgeholt")
            return data
        else:
            logger.warning("Alle Städt könnten nicht erfolgreich geladen")
            return None

    except APIError as e:
        # Fängt Supabase-spezifische Fehler ab (z. B. Duplikate, fehlende Tabellen)
        logger.critical(f"Supabase API-Fehler ({e.code}): {e.message}")
        return None
    except Exception as e:
        # Fängt alle anderen unerwarteten Fehler ab (z. B. Netzwerkprobleme)
        logger.critical(f"Unerwarteter Fehler: {e}")
        return None
    
# Logik, um alle Städte, die gesuchte Stat gehören,aus der Datenbank abzurufen
def get_city_by_country(supabase: Client, country: str):
    try:
        logger.info("request Supebase: get_city_by_country")
        country = country.strip()
        response = supabase.table("cities").select("*").eq("country", country).execute()
        data = response.data
        if data:
            # Erfolgreich abgeholt
            logger.info("Stadt erfolgreich aus der Datenbank abgeholt")
            return data
        else:
             logger.warning("Alle Städt könnten nicht erfolgreich geladen")
             return None
    except APIError as e:
            # Fängt Supabase-spezifische Fehler ab (z. B. Duplikate, fehlende Tabellen)
            logger.critical(f"Supabase API-Fehler ({e.code}): {e.message}")
            return None
    except Exception as e:
            # Fängt alle anderen unerwarteten Fehler ab (z. B. Netzwerkprobleme)
            logger.critical(f"Unerwarteter Fehler: {e}")
            return None
# Logik, um alle Städte aus der Datenbank abzurufen
def get_all_cities(supabase: Client):
    try:
        logger.info("request Supebase: get_all_cities")
        response = supabase.table("cities").select("*").order("id").execute()
        data = response.data
        if data:
            # Erfolgreich abgeholt
            logger.info("Stadt erfolgreich aus der Datenbank abgeholt")
            return data
        else:
            logger.warning("Alle Städt könnten nicht erfolgreich geladen")
            return None
    except APIError as e:
                # Fängt Supabase-spezifische Fehler ab (z. B. Duplikate, fehlende Tabellen)
         logger.critical(f"Supabase API-Fehler ({e.code}): {e.message}")
         return None
    except Exception as e:
                # Fängt alle anderen unerwarteten Fehler ab (z. B. Netzwerkprobleme)
         logger.critical(f"Unerwarteter Fehler: {e}")
         return None
    
def update_city_by_id(supabase: Client,city_id: int, name: Optional[str] = None, country: Optional[str] = None):
    try:
        logger.info("request Supebase: update_city_by_id")
        update_data = {}
        if name is not None:
            update_data["name"] = name.strip()
        if country is not None:
            update_data["country"] = country.strip()    
        response = supabase.table("cities").update(update_data).eq("id", city_id).execute()
        data = response.data
        if data:
            # Erfolgreich abgeholt
            logger.info("Städt könnte erfolgreich updaten/geladen")
            return data
        else:
            logger.warning("Städt könnte nicht erfolgreich updaten/geladen")
            return None
    except APIError as e:
                # Fängt Supabase-spezifische Fehler ab (z. B. Duplikate, fehlende Tabellen)
        logger.critical(f"Supabase API-Fehler ({e.code}): {e.message}")
        return None
    except Exception as e:
                # Fängt alle anderen unerwarteten Fehler ab (z. B. Netzwerkprobleme)
        logger.critical(f"Unerwarteter Fehler: {e}")
        return None