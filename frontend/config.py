import os
from dotenv import load_dotenv
 

# Bestimme den Pfad des aktuellen Skriptverzeichnisses
current_directory = os.path.dirname(os.path.abspath(__file__))

# Konstruiere den vollständigen Pfad zur .env-Datei
dotenv_path = os.path.join(current_directory, '.env')

# Lade Umgebungsvariablen aus der .env-Datei
load_dotenv(dotenv_path)


# Konfigurationseinstellungen für die Anwendung
LANGUAGES = os.getenv("LANGUAGES")
API_URL = os.getenv("API_URL")
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")