from .base import Base, engine
from . import models


def create_tables():
    Base.metadata.create_all(bind=engine)