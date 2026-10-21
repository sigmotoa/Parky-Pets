from select import select

from data.user_db import engine
from models.user import UserBase, UserID, UserUpdate
from sqlmodel import SQLModel, Session, select


def create_user_db(new_user: UserBase):
    session = Session(engine)
    user = UserID.model_validate(new_user)
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()
    return user


def read_all_users_db():
    session = Session(engine)
    users = session.exec(select(UserID)).all()
    session.close()
    return users

def read_one_user_db(user_id: int):
    session = Session(engine)
    user = session.get(UserID, user_id)
    session.close()
    return user


def update_user_db(user_id: int, update: UserUpdate):
    session = Session(engine)

    user = session.get(UserID, user_id)
    user.first_name = update.first_name
    session.add(user)
    session.commit()
    session.refresh(user)

    return user

def delete_user_db(user_id: int):
    session = Session(engine)
    user = session.get(UserID, user_id)
    session.delete(user)
    session.commit()
    #session.refresh(user)
    return user


