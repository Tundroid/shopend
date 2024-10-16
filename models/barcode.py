#!/usr/bin/python
""" Barcode class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Barcode(BaseModel, Base):
    """ Representation of Barcode """
    if models.storage_t == "db":
        __tablename__ = 'barcode'

        barcode = Column(String(50), primary_key=True)
        item = Column(Integer(unsigned=True), ForeignKey('item.id'), nullable=False)

        item_rel = relationship('Item', backref='barcodes')

    def __init__(self, *args, **kwargs):
        """ Barcode initialization """
        super().__init__(*args, **kwargs)
