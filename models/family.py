#!/usr/bin/python
""" Family class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, TIMESTAMP
from sqlalchemy.sql import func


class Family(BaseModel, Base):
    """ Representation of Family """
    if models.storage_t == "db":
        __tablename__ = 'family'

        id = Column(SmallInteger(unsigned=True), primary_key=True, autoincrement=True)
        fam_name = Column(String(50), nullable=False, unique=True)
        fam_desc = Column(Text)
        datetime = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

    def __init__(self, *args, **kwargs):
        """ Family initialization """
        super().__init__(*args, **kwargs)
