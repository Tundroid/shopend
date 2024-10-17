#!/usr/bin/python
""" DepositDetail class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Date, SmallInteger, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class DepositDetail(BaseModel, Base):
    """ Representation of Deposit Detail """
    if models.storage_t == "db":
        __tablename__ = 'deposit_detail'

        batch = Column(String(50), primary_key=True)
        d_date = Column(Date, nullable=False)
        app_user = Column(SmallInteger, ForeignKey('mole_commerce.user_account.id'), nullable=False)
        datetime = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

        user_account = relationship('UserAccount', backref='deposit_details')

    def __init__(self, *args, **kwargs):
        """ DepositDetail initialization """
        super().__init__(*args, **kwargs)
