import os
from dotenv import load_dotenv

import logging 
import logging.config
from pathlib import Path

os.chdir(Path(__file__).parent)
logging.config.fileConfig("./logs/logging.conf", disable_existing_loggers=True)
logger = logging.getLogger() # Root

logger.info("Loading ENV File")
# Bestimme den Pfad des aktuellen Skriptverzeichnisses
current_directory = os.path.dirname(os.path.abspath(__file__))

# Konstruiere den vollständigen Pfad zur .env-Datei
dotenv_path = os.path.join(current_directory, '.env')

# Lade Umgebungsvariablen aus der .env-Datei
load_dotenv(dotenv_path)
logger.debug("Loading ENV File finished")
# Konfigurationseinstellungen für die Anwendung
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

CONNECTIONSTRING = os.getenv("CONNECTIONSTRING")
# PostgreSQL-Verbindungs-URL für SQLAlchemy
DATABASE_URL = f"postgresql://{SUPABASE_KEY}@{SUPABASE_URL}/postgres"
