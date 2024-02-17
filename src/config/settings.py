from dotenv import load_dotenv
import os


DEBUG = True
APP_HOST = os.environ.get("APP_HOST", "127.0.0.1")
APP_PORT = os.environ.get("APP_PORT", 8000)


load_dotenv()


APP_SECRET_KEY = os.environ.get("APP_SECRET_KEY", None)
