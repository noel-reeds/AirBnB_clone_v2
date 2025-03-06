#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


# an association table for many-to-many rlship
place_amenity = Table('place_amenity', Base.metadata,
                    Column('place_id', String(60),
                        ForeignKey('places.id'),
                        primary_key=True,
                        nullable=False),
                    Column('amenity_id',
                        String(60),
                        ForeignKey('amenities.id'),
                        primary_key=True,
                        nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    # switch storage options
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        city_id = Column(String(60), ForeignKey('cities.id',
                                    ondelete='CASCADE'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id',
                                    ondelete='CASCADE'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        user = relationship('User', back_populates='places')
        cities = relationship('City', back_populates='places')
        reviews = relationship('Review', back_populates='place',
                                            passive_deletes=True)
        amenities = relationship('Amenity', secondary=place_amenity,
                    back_populates='place_amenities',viewonly=False)
    else:
        reviews = []

        @property
        def reviews(self):
            """returns the list of Review objs with place_id equals Place.id"""
            from models import storage
            from models.review import Review
            for key, item in storage.all(Review).items():
                if item.id is item.place_id:
                    reviews.append(item)
            return reviews

        def get_amenities(self):
            """returns the list of Amenity instances"""
            return amenities

        amenities = []
        def set_amenities(self):
            """Appends amenities linked to a Place"""
            from models import storage
            from models.amenity import Amenity
            for k, v in storage.all(Amenity).items():
            # all amenities from the same place
            # to be grouped here..
            # logic is incomplete
                if place_amenity.amenity_id is v.id:
                    amenities.append(v)
