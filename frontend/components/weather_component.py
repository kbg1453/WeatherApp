import streamlit as st

def render_weather_dashboard(weather_data: dict):
    """
    Diese Komponente stellt die OpenWeatherMap-Daten in einem 
    modernen Glassmorphism-Design dar.
    """
    if not weather_data or weather_data.get("cod") != 200:
        st.warning("⚠️ Keine gültigen Wetterdaten verfügbar.")
        return

    # 1. Custom CSS für das Design injizieren
    st.markdown("""
        <style>
        .weather-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            padding: 24px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
        .info-box {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 12px;
            padding: 15px;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        .temp-large {
            font-size: 3.5rem;
            font-weight: 700;
            margin: 0;
            line-height: 1;
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. Daten extrahieren
    name = weather_data.get("name", "Unbekannter Ort")
    main_metrics = weather_data.get("main", {})
    weather_info = weather_data.get("weather", [{}])[0]
    coord = weather_data.get("coord", {})
    wind = weather_data.get("wind", {})

    icon_code = weather_info.get("icon", "01d")
    icon_url = f"https://openweathermap.org{icon_code}@4x.png"

    # 3. Haupt-Header & Karte
    st.markdown("### 🌍 Aktuelles Wetter in")
    st.title(name)

    with st.container():
        st.markdown('<div class="weather-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(icon_url, use_container_width=True)
        with col2:
            st.markdown(f'<p class="temp-large">{main_metrics.get("temp", "--")} °C</p>', unsafe_allow_html=True)
            st.markdown(f"#### {weather_info.get('main', 'N/A')}")
            st.caption(f"Zustand: {weather_info.get('description', '').title()}")
        st.markdown('</div>', unsafe_allow_html=True)

    # 4. Detail-Metriken
    st.markdown("### 📊 Details & Luftwerte")
    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("🌡️ **Gefühlt wie**")
        st.markdown(f"### {main_metrics.get('feels_like', '--')} °C")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_b:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("💧 **Feuchtigkeit**")
        st.markdown(f"### {main_metrics.get('humidity', '--')} %")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_c:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("💨 **Windtempo**")
        st.markdown(f"### {wind.get('speed', '--')} m/s")
        st.markdown('</div>', unsafe_allow_html=True)

    # 5. Standort-Karte
    if "lat" in coord and "lon" in coord:
        st.markdown("---")
        st.markdown("📍 **Standort-Koordinaten**")
        map_data = {"lat": [coord["lat"]], "lon": [coord["lon"]]}
        st.map(map_data, height=200)
