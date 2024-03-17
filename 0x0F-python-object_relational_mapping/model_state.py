#!/usr/bin/python3
"""Module containing the class definition of a State and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Class representing a state"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
