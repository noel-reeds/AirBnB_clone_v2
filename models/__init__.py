#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os


# retrieve the storage type
HBNB_TYPE_STORAGE=os.getenv('HBNB_TYPE_STORAGE')

# switch between storage types
if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()

__all__ = [ "state", "amenity", "city",
            "place", "review", "user",
            "base_model"
         ]
