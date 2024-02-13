from dotenv import load_dotenv
import os

load_dotenv()

APP_SECRET_KEY = os.environ.get("APP_SECRET_KEY", None)
