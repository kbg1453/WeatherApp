import streamlit as st
import requests
from config import API_URL  # Importiere die API-URL aus der Konfigurationsdatei

st.title("City Management")

# Hinzufügen einer neuen Stadt
st.header("Add a New City")
city_name = st.text_input("City Name")
country_name = st.text_input("Country Name")

if st.button("Add City"):
    if city_name and country_name:
        # Sende eine POST-Anfrage an den FastAPI-Endpoint
        response = requests.post(
            f"{API_URL}/cities",
            params={ 
                "name": city_name, 
                "country": country_name 
                }
        )
        
        if response.status_code == 200:
            st.success(f"City {city_name} added successfully!")
        else:
            if response.status_code == 422:
                st.error(response.json())
            st.error("Failed to add city. Please try again.")
    else:
        st.error("Please enter both city and country names.")

# Alle Städte anzeigen
st.header("List of Cities")
response = requests.get(f"{API_URL}/cities")
if response.status_code == 200:
    cities = response.json()
    for city in cities:
        st.write(f"City: {city['name']}, Country: {city['country']}")
else:
    st.error("Failed to retrieve cities. Please try again later.")

# Stadt bearbeiten
st.header("Update an Existing City")
city_id = st.number_input("City ID", min_value=0, step=1)
updated_city_name = st.text_input("Updated City Name")
updated_country_name = st.text_input("Updated Country Name")

if st.button("Update City"):
    if city_id and updated_city_name and updated_country_name:
        # Sende eine PUT-Anfrage an den FastAPI-Endpoint
        response = requests.put(
            f"{API_URL}/cities/{city_id}",
           # json={"name": updated_city_name, "country": updated_country_name}
            params={ 
                    "name": updated_city_name, 
                    "country": updated_country_name 
                    }
        )
        
        if response.status_code == 200:
            st.success(f"City ID {city_id} updated successfully!")
        else:
            st.error("Failed to update city. Please try again.")
    else:
        st.error("Please enter city ID, updated city name, and updated country name.")

