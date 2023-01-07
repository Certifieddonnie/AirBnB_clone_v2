#!/usr/bin/python3
"""The Module defines class to manage
Database storage for hbnb clone."""

import os
from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models.review import Review

env = os.getenv('HBNB_ENV')
user = os.getenv('HBNB_MYSQL_USER')
pwd = os.getenv('HBNB_MYSQL_PWD')
host = os.getenv('HBNB_MYSQL_HOST')
db = os.getenv('HBNB_MYSQL_DB')

classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

class DBStorage:
    """The class manages the storage of hbnb models 
    in Sql format.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of the Class."""
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{pwd}@{host}:3306/{db}"
            , pool_pre_ping=True)
        
        if env == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Returns the queried class objects or all
        class objects if cls is none."""
        dct = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                dct[key] = obj
            return dct
        for item in classes.values():
            objs = self.__session.query(item).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                dct[key] = obj
        return dct
    
    def new(self, obj):
        """Adds the object to the current DB session."""
        if obj:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as e:
                self.__session.rollback()
                raise e
    
    def save(self):
        """Commits all changes of the current DB Session."""
        self.__session.commit()
    
    def delete(self, obj=None):
        """delete from the current DB session obj"""
        if obj:
            self.__session.query(type(obj)).filter(type(obj).id == obj.id).delete()
    
    def reload(self):
        """Reloads the Database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine,
                expire_on_commit=False)
        self.__session = scoped_session(Session)()
    
        