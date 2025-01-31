#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import Column, String, relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') is "db":
        cities = relationship('City', back_populates='states',
                                passive_deletes=True)
    else:
        from models import storage
        cities = []
        # retrieve the dictionary of objects
        objs = storage.all()
        for key, item in objs.items():
            if item.id is item.state_id:
                cities.append(item.name)
        return cities
