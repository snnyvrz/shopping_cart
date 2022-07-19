from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from settings import (
    DATABASE,
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_URL,
    DATABASE_PORT,
    DATABASE_NAME,
)

DATABASE_ADDRESS = f"{DATABASE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URL}:{DATABASE_PORT}/{DATABASE_NAME}"
database = Database(DATABASE_ADDRESS)
Base = declarative_base()
engine = create_engine(DATABASE_ADDRESS)


def init_db():
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
