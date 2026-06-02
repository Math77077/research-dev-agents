from dotenv import load_dotenv
import os

load_dotenv()

class SystemSettings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    MODEL_NAME: str = "gemini-2.5-flash"
    TEMPERATURE: float = 0.2