#!/usr/bin/python
""" SupplierType class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, SmallInteger, TIMESTAMP
from sqlalchemy.sql import func


class SupplierType(BaseModel, Base):
    """ Representation of Supplier Type """
    if models.storage_t == "db":
        __tablename__ = 'sup_type'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True)
        st_name = Column(String(50), nullable=False, unique=True)
        st_desc = Column(Text, nullable=False)
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp())

    def __init__(self, *args, **kwargs):
        """ SupplierType initialization """
        super().__init__(*args, **kwargs)
