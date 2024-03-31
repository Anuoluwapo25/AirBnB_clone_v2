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
    if (getenv("HNBN_TYPE_STORAGE") == 'db'):
         __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all delete')
    else:
        name = ''
        cities = []
    
    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self) -> list:
            """
            return list of cities
            """
            my_list = []
            for value in list(models.storage.all("City").value()):
                if (value.state_id == self.id):
                    my_list.append(value)
            return (my_list)
