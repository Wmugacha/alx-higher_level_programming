#!/usr/bin/python3
"""
Script that defines a City class that inherits
from Base class to be used with MySQLAlchemy
ORM.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    City class
    Attributes:
        __tablename__(str): The name of the table
        id (int): Cities id
        name (str): Cities name
        state_id (Int): Foreign key
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
