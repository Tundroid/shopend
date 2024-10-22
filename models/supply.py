#!/usr/bin/python
""" Supply class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, BigInteger
from sqlalchemy.orm import relationship


class Supply(BaseModel, Base):
    """ Representation of Supply """
    if models.storage_t == "db":
        __tablename__ = 'supply'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(BigInteger, primary_key=True, autoincrement=True)
        item = Column(Integer, ForeignKey('mole_commerce.item.id'))
        quantity = Column(Integer, nullable=False)
        unit_cost = Column(Integer, nullable=False)
        expiry = Column(Date, nullable=False)
        batch = Column(String(50),
                       ForeignKey('mole_commerce.supply_detail.batch'))

        # Establish relationships
        item_rel = relationship('Item', backref='supplies')
        batch_rel = relationship('SupplyDetail', backref='supplies')

        # Virtual column (not explicitly defined)
        # total = Column(Integer,
        #               computed=lambda: self.quantity * self.unit_cost)
        # Alternatively, use @hybrid_property
        @property
        def total(self):
            """Computed total cost"""
            return self.quantity * self.unit_cost

    def __init__(self, *args, **kwargs):
        """ Supply initialization """
        super().__init__(*args, **kwargs)
