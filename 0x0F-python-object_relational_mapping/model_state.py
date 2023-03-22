"""
File that defines a State class that inherits
from Base class to be used with MySQLAlchemy
ORM.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State (Base):
    """
    State class
    Attributes:
        __tablename__(str): The name of the table
        id (int): State id
        name (str): State name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name
