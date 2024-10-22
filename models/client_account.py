#!/usr/bin/python
""" ClientAccount class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column, String, SmallInteger, Enum, Boolean, Integer, TIMESTAMP
)
from sqlalchemy.sql import func


class ClientAccount(BaseModel, Base):
    """ Representation of Client Account """
    if models.storage_t == "db":
        __tablename__ = 'client_account'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True)
        acc_name = Column(String(50), nullable=False, unique=True)
        acc_type = Column(Enum('Consumer', 'Worker', 'Both'),
                          nullable=False, default='Consumer')
        is_active = Column(Boolean, nullable=False, default=True)
        credit_limit = Column(Integer, nullable=False, default=25000)
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp())

    def __init__(self, *args, **kwargs):
        """ ClientAccount initialization """
        super().__init__(*args, **kwargs)
