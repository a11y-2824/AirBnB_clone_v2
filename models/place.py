#!/usr/bin/python3
""" Place Module for HBNB project """
from models import storage_type
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship

if storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place',cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,viewonly=False, backref='place_amenities')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ returns list of review instances with place_id == current Place.id
                FileStorage R/ship BTWN Place and Review
            """
            from models import storage
            all_reviews = storage.all(Review)
            lists = []
            for reviews in all_reviews.values():
                if reviews.place_id == self.id:
                    lists.append(reviews)
            return lists

        @property
        def amenities(self):
            """ returns the list of Amenity instances based on amenity_ids with
                all Amenity.id linked to the Place
            """
            from models import storage
            all_amenities = storage.all(Amenity)
            lists = []
            for amenities in all_amenities.values():
                if amenities.id in self.amenity_ids:
                    lists.append(amenities)
            return lists

        @amenities.setter
        def amenities(self, obj):
            """ adding an Amenity.id to attribute amenity_ids. accepts only Amenity
                objects
            """
            if obj is not None:
                if isinstance(obj, Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)
