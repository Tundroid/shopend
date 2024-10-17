#!/usr/bin/python
""" UserAccount class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, SmallInteger, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class UserAccount(BaseModel, Base):
    """ Representation of User Account """
    if models.storage_t == "db":
        __tablename__ = 'user_account'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True)
        acc_type = Column(SmallInteger, ForeignKey('mole_account.acc_type.id'), nullable=False, default=3)
        is_active = Column(Boolean, nullable=False, default=True)
        datetime = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

        acc_type_rel = relationship('AccountType', backref='user_accounts')
        account_rel = relationship('Account', backref='user_account')

    def __init__(self, *args, **kwargs):
        """ UserAccount initialization """
        super().__init__(*args, **kwargs)