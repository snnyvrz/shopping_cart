from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from core.settings import (
    DATABASE,
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_URL,
    DATABASE_PORT,
    DATABASE_NAME,
)

DATABASE_ADDRESS = "{db}://{user}:{password}@{url}:{port}/{name}".format(
    db=DATABASE,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    url=DATABASE_URL,
    port=DATABASE_PORT,
    name=DATABASE_NAME,
)
database = Database(DATABASE_ADDRESS)
Base = declarative_base()
engine = create_engine(DATABASE_ADDRESS)


def init_db():
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
