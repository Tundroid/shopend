#!/usr/bin/python
""" Item class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column, String, Integer, SmallInteger, ForeignKey, Boolean, TIMESTAMP
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Item(BaseModel, Base):
    """ Representation of Item """
    if models.storage_t == "db":
        __tablename__ = 'item'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(Integer, primary_key=True, autoincrement=True)
        item_name = Column(String(50), nullable=False, unique=True)
        item_cat = Column(SmallInteger,
                          ForeignKey('mole_commerce.item_cat.id'),
                          nullable=False, default=1)
        cost_price = Column(Integer, nullable=False, default=0)
        selling_price = Column(Integer, nullable=False, default=0)
        min_sell_price = Column(Integer, nullable=False, default=0)
        min_order_qty = Column(Integer, nullable=False, default=5)
        family = Column(SmallInteger,
                        ForeignKey('mole_commerce.family.id'),
                        nullable=False, default=1)
        sector = Column(SmallInteger,
                        ForeignKey('mole_commerce.sector.id'),
                        nullable=False, default=1)
        is_active = Column(Boolean, nullable=False, default=True)
        is_metered = Column(Boolean, nullable=False, default=True)
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp())

        item_cat_rel = relationship('ItemCategory', backref='items')
        family_rel = relationship('Family', backref='items')
        sector_rel = relationship('Sector', backref='items')

    def __init__(self, *args, **kwargs):
        """ Item initialization """
        super().__init__(*args, **kwargs)
