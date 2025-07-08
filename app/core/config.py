from dotenv import load_dotenv
import os

load_dotenv()

APILAYER_API_KEY = os.getenv("APILAYER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
