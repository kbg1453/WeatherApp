from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import city_routes, city_weather_routes

# Erstellt eine FastAPI-Anwendung
app = FastAPI()

# Konfiguriert CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Erlaube alle Ursprünge, passe dies in der Produktion an
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registriert die API-Routen
app.include_router(city_routes.router) 
app.include_router(city_weather_routes.router)

# Startpunkt der Anwendung
@app.get("/")
async def root():
    return {"message": "Welcome to the Weather API"}
