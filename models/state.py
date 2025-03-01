#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship as rs


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    cities = ""
    name = ""
    # for db_storage db, configure database.
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = rs('City', back_populates='state', passive_deletes=True)
    else:
        cities = []

        @property
        def cities(self):
            from models import storage
            from models.city import City
            cities = []
            # retrieve the dictionary of objects
            for key, item in storage.all(City).items():
                if item.id is item.state_id:
                    cities.append(item.name)
            return cities
