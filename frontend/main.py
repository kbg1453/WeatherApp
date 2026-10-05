import streamlit as st
import requests
from components.select_box_component import select_city, select_language
from config import LANGUAGES, API_URL, OPENWEATHERMAP_API_KEY, DISCORD_WEBHOOK_URL
from components.weather_component import render_weather_dashboard


# Funktion zum Abrufen von Wetterdaten
def fetch_weather(city_name,country,language ):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country}&appid={OPENWEATHERMAP_API_KEY}&units=metric&lang={language}"
    response = requests.get(url)
    return response.json()

# Funktion zum Senden einer Discord-Nachricht
def send_discord_message(content):
    data = {"content": content}
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    return response.status_code

st.title("City and Language Selector")

# Auswahl der Stadt über die API
response = requests.get(f"{API_URL}/cities/")
cities = response.json()
# --- Layout: 2 Spalten nebeneinander (Stadt ist doppelt so breit wie Sprache) ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🏙️ Stadtauswahl")
    selected_city_id, selected_city_name, selected_country = select_city(cities)
    st.caption(f"Ausgewählte Stadt: **{selected_city_name}**")

with col2:
    st.markdown("### 🌐 Sprache")
    selected_language_name, selected_language_code = select_language(LANGUAGES)
    st.caption(f"Sprache: **{selected_language_name}**")

# --- Button unter den Spalten ---
st.markdown("---") # Optionale Trennlinie für eine saubere Struktur

# Button zum Abrufen und Speichern der Wetterdaten
if st.button("🌦️ Wetterdaten abrufen", use_container_width=True):
    with st.spinner(f"Lade Wetter für {selected_city_name}..."):
        weather_data = fetch_weather(selected_city_name,selected_country,selected_language_code)
        #st.write("Wetterdaten:", weather_data)

        render_weather_dashboard(weather_data)
        weather_info = weather_data.get("weather", [{}])[0]
        main_metrics = weather_data.get("main", {})
        
        # Speichere die Wetterdaten in Supabase
        response = requests.post(f"{API_URL}/weather/", 
                                 params={ 
                                        "city_id": selected_city_id,
                                        "temperature": main_metrics.get("temp", "--"),
                                        "weather_description": weather_info.get('description', '')           
                                        }
                                 )
        if response.status_code == 200:
            # Sende eine Nachricht an Discord
            discord_status = send_discord_message(f"Wetterdaten für {selected_city_name} wurden aktualisiert und gespeichert.")
            if discord_status == 204:
                st.success("Daten abgeholt, Datenbank gespeichert und Discord gemeldet!")
            else:
                st.error("Fehler beim Senden der Discord-Nachricht.")
        else:
            st.error("Fehler beim Speichern der Wetterdaten.")