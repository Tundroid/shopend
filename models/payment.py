#!/usr/bin/python
""" Payment class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, SmallInteger, String, Date, Text, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Payment(BaseModel, Base):
    """ Representation of Payment """
    if models.storage_t == "db":
        __tablename__ = 'payment'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(Integer, primary_key=True, autoincrement=True)
        invoice = Column(String(50), ForeignKey('mole_commerce.record_detail.batch'))
        amount = Column(Integer, nullable=False)
        pay_date = Column(Date, nullable=False)
        is_instant = Column(Boolean, nullable=False, default=True)
        mode = Column(SmallInteger, ForeignKey('mole_commerce.pay_mode.id'), default=1)
        app_user = Column(SmallInteger, ForeignKey('mole_commerce.user_account.id'))
        pay_desc = Column(Text)
        datetime = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

        # Establish relationships
        invoice_rel = relationship('RecordDetail', backref='payments')
        mode_rel = relationship('PayMode', backref='payments')
        app_user_rel = relationship('UserAccount', backref='payments')

    def __init__(self, *args, **kwargs):
        """ Payment initialization """
        super().__init__(*args, **kwargs)
