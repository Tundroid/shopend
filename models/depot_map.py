#!/usr/bin/python
""" DepotMap class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column, SmallInteger, ForeignKey, PrimaryKeyConstraint
)
from sqlalchemy.orm import relationship


class DepotMap(BaseModel, Base):
    """ Representation of Depot Map """
    if models.storage_t == "db":
        __tablename__ = 'depot_map'
        __table_args__ = {'schema': 'mole_commerce'}

        source = Column(SmallInteger,
                        ForeignKey('mole_commerce.depot_detail.id'),
                        nullable=False)
        destination = Column(SmallInteger,
                             ForeignKey('mole_commerce.depot_detail.id'),
                             nullable=False)
        operation = Column(SmallInteger,
                           ForeignKey('mole_commerce.operation.id'),
                           nullable=False)

        __table_args__ = (
            PrimaryKeyConstraint('source', 'destination', 'operation'),
        )

        depot_source_rel = relationship('DepotDetail', foreign_keys=[source],
                                        backref='depot_map_sources')
        depot_destination_rel = relationship('DepotDetail',
                                             foreign_keys=[destination],
                                             backref='depot_map_destinations')
        operation_rel = relationship('Operation', backref='depot_maps')

    def __init__(self, *args, **kwargs):
        """ DepotMap initialization """
        super().__init__(*args, **kwargs)
