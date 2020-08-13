#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""

"""Task 10"""
# from models.base_model import BaseModel ,Base
# from models.place import place_amenity
# from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship
# import os


# class Amenity(BaseModel, Base):
#     """class Amenity"""
#     __tablename__ = 'amenities'
#     if os.getenv("HBNB_TYPE_STORAGE") == "db":

#         name = Column(String(128), nullable=False)
#         place_amenities = relationship('Place', secondary=place_amenity, viewonly=False)

#     else:

#         name = ""
