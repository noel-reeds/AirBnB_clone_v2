#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = ""
    # maps model  to db storage
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        from models.place import place_amenity
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity,
                back_populates='amenities')
