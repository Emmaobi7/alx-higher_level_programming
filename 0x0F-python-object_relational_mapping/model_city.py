#!/usr/bin/python3
"""builds a table city in db"""

from sqlalchemy import create_engine, Integer, String, Column
from model_state import Base





class City(Base):
    """
    city: datasae table
    (Base): sqlalchemy base class
    """

    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, primaey_key=True, nullable=False)

