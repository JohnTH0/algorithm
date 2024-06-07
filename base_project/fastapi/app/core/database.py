from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_HOST:str = config("DB_HOST")
DB_PORT:str = config("DB_PORT")
DB_USER:str = config("DB_USER")
DB_PASSWORD:str = config("DB_PASSWORD")
DB_NAME:str = config("DB_NAME")

SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}:{}/{}".format(DB_USER,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
