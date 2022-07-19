import os

from dotenv import load_dotenv

load_dotenv()

# Database
DATABASE = os.getenv("DATABASE")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")
