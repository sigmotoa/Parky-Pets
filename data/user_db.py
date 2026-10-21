from sqlmodel import SQLModel, create_engine, Session

database_name = "user.db"
database_path = f"sqlite:///{database_name}"

engine = create_engine(database_path)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

