#!/usr/bin/python
""" ItemCategory class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, TIMESTAMP, SmallInteger
from sqlalchemy.sql import func


class ItemCategory(BaseModel, Base):
    """ Representation of Item Category """
    if models.storage_t == "db":
        __tablename__ = 'item_cat'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True)
        cat_name = Column(String(50), nullable=False, unique=True)
        cat_desc = Column(Text)
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp())

    def __init__(self, *args, **kwargs):
        """ ItemCategory initialization """
        super().__init__(*args, **kwargs)
