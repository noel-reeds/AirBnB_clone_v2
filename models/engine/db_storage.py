#!/usr/bin/env python3
"""DB Storage Module for the HBnB"""
import os
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

Base = declarative_base()

class DBStorage:
    """DB Storage - SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Handles instance creation"""
        # creates a URL for engine create without escaping chars
        engine_url = URL.create(
            "mysql+mysqldb",
            HBNB_MYSQL_USER=os.getenv('HBNB_MYSQL_USER'),
            HBNB_MYSQL_PWD=os.getenv('HBNB_MYSQL_PWD'),
            HBNB_MYSQL_HOST=os.getenv('HBNB_MYSQL_HOST'),
            HBNB_MYSQL_DB=os.getenv('HBNB_MYSQL_DB'),
        )
        # creates engine
        self.__engine = create_engine(engine_url, pool_pre_ping=True)

        # drop all tables if env is set to 'test'
        HBNB_ENV = os.getenv(HBNB_ENV)
        if HBNB_ENV is 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        if cls:
            objs = self.__session.query(cls).all()
            return objs
        else:
            objs = self.__session.query(
                           User, State, City,
                           Amenity, Place, Review
                           ).all()
            return objs

    def new(self, obj):
        """Add the object to the current db session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current db session"""
        self._session.commit()

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
        Base.metadata.create_all(self.__engine)
        some_scope = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(some_scope)
        self.__session = Session()
