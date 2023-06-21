#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models import storage_type
from models.city import City
from sqlalchemy.orm import relationship
class State(BaseModel, Base):
    """ State class and Table Model"""
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            """
            returning the list of City instances with state_id == current State.id
            FileStorage relationship BTWN State and City
            """
            from models import storage
            related = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related.append(city)
            return related
