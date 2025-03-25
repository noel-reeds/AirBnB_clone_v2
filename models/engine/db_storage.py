#!/usr/bin/python3
"""DB Storage Module for the HBnB"""
import os
from sqlalchemy import create_engine, URL
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """DB Storage - SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Handles instance creation"""
        # creates a URL for engine create without escaping chars
        engine_url = URL.create(
            "mysql+mysqldb",
            username=os.getenv('HBNB_MYSQL_USER'),
            password=os.getenv('HBNB_MYSQL_PWD'),
            host=os.getenv('HBNB_MYSQL_HOST'),
            database=os.getenv('HBNB_MYSQL_DB'),
        )
        # creates engine
        self.__engine = create_engine(engine_url, pool_pre_ping=True)

        # drop all tables if env is set to 'test'
        HBNB_ENV = os.getenv('HBNB_ENV')
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        if cls:
            objs = {}
            res = self.__session.query(cls).all()
            for obj in res:
                """
                if obj._sa_instance_state:
                    del obj._sa_instance_state
                """
                key = f'{obj.__class__.__qualname__}.{obj.id}'
                objs[key] = obj
            return objs
        else:
            res = self.__session.query(State, City).all()
            # modify res into a dictionary and return
            return

    def new(self, obj):
        """Add the object to the current db session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from current db session"""
        if obj:
            self.__session.delete(obj)
        else:
            return

    def reload(self):
        """Create all tables in the database"""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place, place_amenity
        from models.review import Review
        from models.amenity import Amenity
        Base.metadata.create_all(self.__engine)
        some_scope = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(some_scope)
        self.__session = Session()

    def close(self):
        """discards a session"""
        self._DBStorage__session.close()
