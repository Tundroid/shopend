#!/usr/bin/python
""" Depot class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, SmallInteger, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship


class Depot(BaseModel, Base):
    """ Representation of Depot """
    if models.storage_t == "db":
        __tablename__ = 'depot'

        depot_id = Column(SmallInteger, ForeignKey('depot_detail.id'), nullable=False)
        item_id = Column(Integer(unsigned=True), ForeignKey('item.id'), nullable=False)
        stock = Column(Integer, nullable=False, default=0)

        __table_args__ = (
            PrimaryKeyConstraint('depot_id', 'item_id'),
        )

        depot_rel = relationship('DepotDetail', backref='depot_stock')
        item_rel = relationship('Item', backref='depot_stock')

    def __init__(self, *args, **kwargs):
        """ Depot initialization """
        super().__init__(*args, **kwargs)
