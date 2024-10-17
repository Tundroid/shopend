#!/usr/bin/python
""" SupplyDetail class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, SmallInteger, Integer, Date, Text, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class SupplyDetail(BaseModel, Base):
    """ Representation of Supply Detail """
    if models.storage_t == "db":
        __tablename__ = 'supply_detail'
        __table_args__ = {'schema': 'mole_commerce', 'primary_key': None}

        batch = Column(String(50), primary_key=True, unique=True)
        supplier = Column(SmallInteger, ForeignKey('mole_commerce.supplier.id'))
        sup_date = Column(Date, nullable=False)
        receiver = Column(Integer, ForeignKey('mole_commerce.client_account.id'))
        ref = Column(String(50), nullable=False)
        app_user = Column(Integer, ForeignKey('mole_commerce.user_account.id'))
        is_stocked = Column(Boolean, nullable=False, default=False)
        sup_desc = Column(Text)
        datetime = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

        # Establish relationships
        supplier_rel = relationship('Supplier', backref='supply_details')
        receiver_rel = relationship('ClientAccount', backref='supply_details')
        app_user_rel = relationship('UserAccount', backref='supply_details')

    def __init__(self, *args, **kwargs):
        """ SupplyDetail initialization """
        super().__init__(*args, **kwargs)
