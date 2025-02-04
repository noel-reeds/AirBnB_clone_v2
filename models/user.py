#!/usr/bin/python3
"""This module defines a class User"""
import os
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    # configure storage options
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship('Place', back_populates='user',
                                                passive_deletes=True)
