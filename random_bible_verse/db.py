from sqlmodel import create_engine, SQLModel

from random_bible_verse import models

engine = create_engine("sqlite:///bibles.db")


def create_db_tables():
    SQLModel.metadata.create_all(engine)
