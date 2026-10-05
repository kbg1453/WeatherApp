#Erstelle eine neue Komponente für die Auswahlboxen.
import streamlit as st

def select_city(cities):
    
    city_list =[]
    for city in cities:
        id,name,country  = city['id'],city['name'],city['country']
        city_list.append((id,name,country))
    
    city_names = [name for  id, name, country in city_list]
    
    selected_city_name = st.selectbox("Wähle eine Stadt:", city_names)
    selected_city_country = next(country for id, name, country in city_list if name == selected_city_name)
    selected_city_id= next(id for id, name, country in city_list if name == selected_city_name)
    return selected_city_id,selected_city_name, selected_city_country
    

def select_language(languages):
    # Splitte die Sprachen in eine Liste von Tupeln (Name, Code)
    language_list = [lang.split(':') for lang in languages.split(',')]
    
    # Erstelle eine Liste der Sprachnamen für die Auswahl
    language_names = [name for name, code in language_list]
    
    # Verwende Streamlit's selectbox, um eine Sprache auszuwählen
    selected_name = st.selectbox("Wähle eine Sprache:", language_names)
    
    # Finde den Sprachcode, der dem ausgewählten Namen entspricht
    selected_code = next(code for name, code in language_list if name == selected_name)
    
    return selected_name,selected_code

