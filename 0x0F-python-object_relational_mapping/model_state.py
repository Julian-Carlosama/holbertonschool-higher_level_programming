#!/usr/bin/python3
""" Class used in ORM """
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

""" Model for the class that runs the ORM """


class State(Base):
    """ Method that define the table name """
    __tablename__ = 'states'

    """ Atributes for the table """
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
