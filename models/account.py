#!/usr/bin/python
""" Account class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, SmallInteger, String, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Account(BaseModel, Base):
    """ Representation of Account """
    if models.storage_t == "db":
        __tablename__ = 'account'
        __table_args__ = {'schema': 'mole_account'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True)
        acc_name = Column(String(50), nullable=False, unique=True)
        acc_pwd = Column(String(256), nullable=False, default='molecule')
        acc_type = Column(SmallInteger, ForeignKey('acc_type.id'), nullable=False, default=3)
        is_active = Column(Boolean, nullable=False, default=True)
        datetime = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

        acc_type_rel = relationship('AccountType', backref='accounts')

    def __init__(self, *args, **kwargs):
        """ Account initialization """
        super().__init__(*args, **kwargs)
