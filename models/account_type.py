#!/usr/bin/python
""" AccountType class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, SmallInteger, String


class AccountType(BaseModel, Base):
    """ Representation of Account Type """
    if models.storage_t == "db":
        __tablename__ = 'acc_type'
        __table_args__ = {'schema': 'mole_account'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True)
        type_name = Column(String(50), nullable=False, unique=True)

    def __init__(self, *args, **kwargs):
        """ AccountType initialization """
        super().__init__(*args, **kwargs)
