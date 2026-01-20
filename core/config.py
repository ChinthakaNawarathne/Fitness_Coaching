import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file if present

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Set it in .env or as environment variable.")

os.environ["GROQ_API_KEY"] = GROQ_API_KEY