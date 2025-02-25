#!/usr/bin/python3
""" City Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = ""
    name = ""
    # configure database for db_storage
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        state_id = Column(String(60),
                   ForeignKey('states.id', ondelete='CASCADE'), nullable=False)
        name = Column(String(128), nullable=False)
        state = relationship('State', back_populates='cities')
        places = relationship('Place', back_populates='cities',
                                                passive_deletes=True)
    else:
        from models.state import State
        state_id = State.id
