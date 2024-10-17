#!/usr/bin/python
""" PayMode class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, SmallInteger, Boolean, TIMESTAMP
from sqlalchemy.sql import func


class PayMode(BaseModel, Base):
    """ Representation of Pay Mode """
    if models.storage_t == "db":
        __tablename__ = 'pay_mode'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True)
        mode_name = Column(String(50), nullable=False, unique=True)
        is_active = Column(Boolean, nullable=False, default=True)
        datetime = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

    def __init__(self, *args, **kwargs):
        """ PayMode initialization """
        super().__init__(*args, **kwargs)
