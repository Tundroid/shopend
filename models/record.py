#!/usr/bin/python
""" Record class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Record(BaseModel, Base):
    """ Representation of Record """
    if models.storage_t == "db":
        __tablename__ = 'record'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(BigInteger, primary_key=True, autoincrement=True)
        item = Column(Integer, ForeignKey('mole_commerce.item.id'))
        quantity = Column(Integer, nullable=False)
        source_stock = Column(Integer, nullable=False)
        dest_stock = Column(Integer, nullable=False)
        amount = Column(Integer, nullable=False)
        batch = Column(String(50),
                       ForeignKey('mole_commerce.record_detail.batch'))

        # Establish relationships
        item_rel = relationship('Item', backref='records')
        batch_rel = relationship('RecordDetail', backref='records')

        # Virtual column (not explicitly defined)
        @property
        def total(self):
            """Computed total amount"""
            return self.quantity * self.amount

    def __init__(self, *args, **kwargs):
        """ Record initialization """
        super().__init__(*args, **kwargs)
