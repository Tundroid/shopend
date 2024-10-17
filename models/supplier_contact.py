#!/usr/bin/python
""" SupplierContact class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, SmallInteger, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class SupplierContact(BaseModel, Base):
    """ Representation of Supplier Contact """
    if models.storage_t == "db":
        __tablename__ = 'sup_contact'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True)
        con_name = Column(String(50), nullable=False, unique=True)
        con_phone = Column(String(50), nullable=False)
        con_email = Column(String(50), nullable=False)
        supplier = Column(SmallInteger, ForeignKey('mole_commerce.supplier.id'), nullable=False)
        datetime = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

        supplier_rel = relationship('Supplier', backref='sup_contacts')

    def __init__(self, *args, **kwargs):
        """ SupplierContact initialization """
        super().__init__(*args, **kwargs)
