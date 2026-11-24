from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv

load_dotenv()

#DATABASE_URL_NEON = os.getenv('DATABASE_URL')

DATABASE_URL_NEON = (
f"postgresql+psycopg://"
f"{os.getenv('PGUSER')}:{os.getenv('PGPASSWORD')}"
f"@{os.getenv('PGHOST')}/{os.getenv('PGDATABASE')}"
f"?sslmode={os.getenv('PGSSLMODE', 'require')}"
f"&channel_binding={os.getenv('PGCHANNELBINDING', 'require')}")


database_name = "parkypets.db"
database_url = f"sqlite:///{database_name}"

engine = create_engine(DATABASE_URL_NEON)

def create_db_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session