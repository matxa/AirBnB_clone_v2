#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session

# engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
#                        sys.argv[1], sys.argv[2], sys.argv[3]),
#                        pool_pre_ping=True)

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
