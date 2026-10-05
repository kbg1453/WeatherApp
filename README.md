# WeatherApp – Wetter- und Kommunikationsplattform

Dieses Projekt integriert mehrere Technologien, um Wetterdaten abzurufen, sicher in der Cloud zu speichern und über eine interaktive Webanwendung sowie über Discord bereitzustellen.

Das Backend nutzt **FastAPI**, um eine RESTful API zu betreiben, welche die aktuellen Wetterdaten von der **OpenWeatherMap API** bezieht und in einer **Supabase-Datenbank** hinterlegt. Ein **Discord-Bot** (via Webhook) sendet automatisierte Updates direkt auf deine Server, während eine **Streamlit-Anwendung** als benutzerfreundliches Frontend zur Visualisierung dient.

---

## 🛠️ Verwendete Technologien

* **FastAPI:** Erstellung der performanten Backend-API.
* **OpenWeatherMap API:** Abruf von weltweiten Echtzeit-Wetterdaten.
* **Supabase:** Cloud-Datenbank zum Speichern von Wetter- und Benutzerdaten.
* **Discord Webhooks:** Schnelle Bereitstellung von Wetter-Updates auf Discord-Servern.
* **Streamlit:** Erstellung des interaktiven und responsiven Web-Frontends.

---

## 🚀 Installation & Setup

### 1. Repository klonen oder Daten kopieren
Lade das Projekt herunter oder klone es mit Git in dein lokales Verzeichnis:
```bash
git clone https://github.com/kbg1453/WeatherApp
cd WeatherApp
```

### 2. Virtuelle Umgebung (venv) erstellen
Erstelle eine isolierte Python-Umgebung und aktiviere sie:

**Unter Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Unter macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 🔑 Umgebungsvariablen konfigurieren (.env)

Das Projekt benötigt API-Schlüssel und Zugangsdaten. Erstelle dazu zwei separate `.env`-Dateien im Projektverzeichnis.

### Frontend-Konfiguration (`frontend/.env`)
Erstelle diese Datei im Ordner `frontend/` und füge deine Schlüssel hinzu:

```env
# OpenWeatherMap API-Key erhalten unter: https://home.openweathermap.org/users/sign_up
OPENWEATHERMAP_API_KEY=dein_openweathermap_api_key

# Discord Webhook-URL deines Discord-Servers: https://discord.com/
DISCORD_WEBHOOK_URL="deine_discord_webhook_url"

# API-Verbindung zum lokalen Backend
API_URL="http://127.0.0.1:8000"

# Sprachkonfiguration (Nutzt zweistellige ISO-3166-1-Kurzformen)
# Wichtig: Wenn du neue Städte oder Sprachen hinzufügst, verwende immer die offiziellen ISO-Codes!
# Beispiele: de = Deutschland, gb = England/Großbritannien, tr = Türkei
LANGUAGES="English:gb,Deutsch:de,Türkçe:tr"
```

### Backend-Konfiguration (`backend/.env`)
Erstelle diese Datei im Ordner `backend/` für die Datenbankverbindung:

```env
# Supabase Zugangsdaten erhalten unter: https://supabase.com/docs/reference/api/v1-create-project-api-key
SUPABASE_URL=deine_supabase_url
SUPABASE_KEY=dein_supabase_key
```

---

## 🏃‍♂️ Anwendung ausführen

Stelle sicher, dass deine virtuelle Umgebung aktiviert ist. Starte anschließend das Backend und das Frontend in zwei separaten Terminal-Fenstern:

### 1. Backend starten (FastAPI)
```bash
uvicorn backend.main:app --reload
```
Das Backend ist nun unter `http://127.0.0.1:8000` erreichbar.

### 2. Frontend starten (Streamlit)
```bash
streamlit run frontend/main.py
```
Die Webanwendung öffnet sich automatisch in deinem Browser.

---

## 🌍 Wichtiger Hinweis zu Ländern & Sprachen
Wenn du dem System **neue Städte oder Sprachen** hinzufügst, musst du zwingend die standardisierte **Länder-Kurzform (ISO-3166-1-Alpha-2)** verwenden. 
* **Falsch:** `england`, `eng`, `germany`, `deu`
* **Richtig:** `de` (Deutschland), `gb` (Großbritannien/England), `tr` (Türkei), `us` (Vereinigte Staaten)
