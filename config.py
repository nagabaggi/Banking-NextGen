import os

class Config:
    PORT = 3978
    APP_ID = os.getenv("MICROSOFT_APP_ID", "BH01074739@devcorptenant.com")
    APP_PASSWORD = os.getenv("MICROSOFT_APP_PASSWORD", "Gurudeva25$apr")