#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    # for db_storage db, configure database.
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='state',
                                passive_deletes=True)
    else:
        name = ""
        cities = []
    
    @property
    def cities(self):
        from models import storage
        cities = []
        # retrieve the dictionary of objects
        for key, item in storage.all(City).items():
            if item.id is item.state_id:
                cities.append(item.name)
        return cities
