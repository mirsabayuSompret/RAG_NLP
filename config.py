from dotenv import load_dotenv
import os

load_dotenv()

class Config: 
    HF_TOKEN = os.getenv('HF_TOKEN')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    EMBEDDING_MODEL = "BAAI/bge-m3"
    LLM_MODEL = "gemini-3.1-flash-lite"
    CHUNK_SIZE = 150
    CHUNK_OVERLAP = 30

    @classmethod
    def validate(cls):
        if not cls.HF_TOKEN:
            raise ValueError("HF_TOKEN not found in env files")
        if not cls.GEMINI_API_KEY:
            raise ValueError("GEMINI API KEY not found in env files")
        print (' all api key is loaded successfully')