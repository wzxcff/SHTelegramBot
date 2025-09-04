from dotenv import load_dotenv
from os import getenv as env
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DB_URL = f"postgresql+psycopg2://{env("DB_USERNAME")}:{env("DB_PASSWORD")}@localhost:5432/{env('DB_NAME')}"

engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
