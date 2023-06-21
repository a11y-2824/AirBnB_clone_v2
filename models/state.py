#!/usr/bin/python3
""" This is the state Module """
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
        cities = relationship(
             'City', backref='state', cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            """
            returns the list of City instances with state_id
            FileStorage relationship between State and City
            """
            from models import storage
            related = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related.append(city)
            return related
