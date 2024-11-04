import os


class Settings:
    def __init__(self):
        self.API_BASE = "https://cloud.digitalocean.com/gen-ai"
        self.AGENT_ID = os.getenv("DATA_AGENT_ID")
        self.AGENT_KEY = os.getenv("DATA_CHATBOT_ID")
        self.AGENT_ENDPOINT = os.getenv("AGENT_ENDPOINT")


# Global variable to import settings
settings = Settings()
