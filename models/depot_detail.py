#!/usr/bin/python
""" DepotDetail class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, Enum, Boolean, TIMESTAMP, SmallInteger
from sqlalchemy.sql import func


class DepotDetail(BaseModel, Base):
    """ Representation of DepotDetail """
    if models.storage_t == "db":
        __tablename__ = 'depot_detail'
        __table_args__ = {'schema': 'mole_commerce'}

        id = Column('id', SmallInteger, primary_key=True, autoincrement=True)
        depot_name = Column(String(50), nullable=False, unique=True)
        depot_desc = Column(Text, nullable=False)
        depot_type = Column(Enum('Source', 'Destination', 'Both'), nullable=False)
        is_metered = Column(Boolean, nullable=False, default=True)
        datetime = Column(TIMESTAMP, nullable=False, server_default=func.current_timestamp())

    def __init__(self, *args, **kwargs):
        """ DepotDetail initialization """
        super().__init__(*args, **kwargs)
