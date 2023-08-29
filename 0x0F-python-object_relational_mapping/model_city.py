#!/usr/bin/python3
"""builds a table city in db"""

from sqlalchemy import create_engine, Integer, String, Column, ForeignKey
from model_state import Base


class City(Base):
    """
    city: datasae table
    (Base): sqlalchemy base class
    """

    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
