#!/usr/bin/python
""" Sector class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, SmallInteger, TIMESTAMP
from sqlalchemy.sql import func


class Sector(BaseModel, Base):
    """ Representation of Sector """
    if models.storage_t == "db":
        __tablename__ = 'sector'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True)
        sec_name = Column(String(50), nullable=False, unique=True)
        sec_desc = Column(Text)
        datetime = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

    def __init__(self, *args, **kwargs):
        """ Sector initialization """
        super().__init__(*args, **kwargs)
