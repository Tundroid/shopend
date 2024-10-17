#!/usr/bin/python
""" Supplier class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, SmallInteger, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Supplier(BaseModel, Base):
    """ Representation of Supplier """
    if models.storage_t == "db":
        __tablename__ = 'supplier'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True)
        sup_name = Column(String(50), nullable=False, unique=True)
        sup_type = Column(SmallInteger, ForeignKey('mole_commerce.sup_type.id'), nullable=False)
        sup_desc = Column(Text)
        datetime = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

        sup_type_rel = relationship('SupplierType', backref='suppliers')

    def __init__(self, *args, **kwargs):
        """ Supplier initialization """
        super().__init__(*args, **kwargs)
