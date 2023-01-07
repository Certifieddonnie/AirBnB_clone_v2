#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.city import City

stor_type = os.getenv('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if stor_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")
    else:
         name = ''
    
    @property
    def cities(self):
        """returns the list of City instances.
        File Storage relationship between State and City.
        """
        from models import storage
        city_list = []
        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
