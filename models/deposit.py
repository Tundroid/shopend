#!/usr/bin/python
""" Deposit class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Deposit(BaseModel, Base):
    """ Representation of Deposit """
    if models.storage_t == "db":
        __tablename__ = 'deposit'
        __table_args__ = {'schema': 'mole_commerce'}

        payment = Column(Integer, ForeignKey('mole_commerce.payment.id'),
                         primary_key=True)
        batch = Column(String(50),
                       ForeignKey('mole_commerce.deposit_detail.batch'))

        # Establish relationships
        payment_rel = relationship('Payment', backref='deposit')
        batch_rel = relationship('DepositDetail', backref='deposits')

    def __init__(self, *args, **kwargs):
        """ Deposit initialization """
        super().__init__(*args, **kwargs)
