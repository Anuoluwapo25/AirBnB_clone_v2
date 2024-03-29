#!/usr/bin/python3
"""
State Class from Models Module
"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float
import models
storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """State class handles all application states"""
        __tablename__ = 'states'
        if (os.getenv("HNBN_TYPE_STORAGE") == 'db'):
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all delete')
    else:
        name = ''

        @property
        def cities(self):
            """
            return list of cities
            """
            my_list = []
            for key, value in models.storage.all("City"):
                if (value.state_id == self.id):
                    my_list.append(value)
            return (my_list)
