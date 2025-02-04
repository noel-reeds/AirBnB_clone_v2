#!/usr/bin/python3
""" Review module for the HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = ""
    user_id = ""
    text = ""
    # switch storage options
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60),
                    ForeignKey('places.id', ondelete='CASCADE'), nullable=False)
        place = relationship('Place', back_populates='reviews')
        user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'),
                                                    nullable=False)
        user = relationship('User', back_populates='reviews')
