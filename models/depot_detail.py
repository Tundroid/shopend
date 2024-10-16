#!/usr/bin/python
""" DepotDetail class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, DateTime, Text
from sqlalchemy.orm import relationship
import uuid
import datetime


class DepotDetail(BaseModel, Base):
    """ Representation of DepotDetail """
    if models.storage_t == "db":
        __tablename__ = 'depot_detail'

        id = Column(Integer, primary_key=True)
        depot_name = Column(String(50), ForeignKey('admin.admin_id'), nullable=False)
        depot_desc = Column(Text)
        depot_type = Column(Text(30))
        # is_metered = Column(, default=datetime.datetime.utcnow())
        datetime = Column(DateTime, default=datetime.datetime.utcnow())
    else:
        pass

    def __init__(self, *args, **kwargs):
        """ DepotDetails initialization """
        super().__init__(*args, **kwargs)