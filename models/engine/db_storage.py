#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from sys import argv
import os
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import MySQLdb

classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
          }

Base = declarative_base()

class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')       

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(user, password, host, database),
            pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """querry current database session"""
        self.__session = Session(self.__engine)
        dictionary = {}
        if cls:
            dictionary = self.__session.query(cls).all()
        else:
            dictionary = self.__session.query(classes.values()).all()

        return dictionary
        
    def new(self, obj):
        """ add obj to curr db """
        self.__session = Session(self.__engine)

        if obj:
            self.__session.add(obj)

    def save(self):
        """ save changes to database """
        self.__session.commit()
    
    def delete(self, obj=None):
        """ delete given obj """
        if obj is not None:
            self.__session.delete(obj) 

    def reload(self):
        """ reload """
        self.__session = Session(self.__engine)
        Base.metadata.create_all(__engine)

    def close(self)
        """closes session"""
        self.__session.close()
