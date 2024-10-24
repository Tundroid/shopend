#!/usr/bin/python
""" Operation class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, CHAR, Text, SmallInteger


class Operation(BaseModel, Base):
    """ Representation of Operation """
    if models.storage_t == "db":
        __tablename__ = 'operation'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column(SmallInteger, primary_key=True, autoincrement=True)
        op_name = Column(String(50), nullable=False, unique=True)
        op_sign = Column(CHAR(1), nullable=False, default='+')
        op_desc = Column(Text, nullable=False)
    else:
        pass

    def __init__(self, *args, **kwargs):
        """ Operation initialization """
        super().__init__(*args, **kwargs)
