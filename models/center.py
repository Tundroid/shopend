#!/usr/bin/python
""" Center class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, UniqueConstraint, Boolean


class Center(BaseModel, Base):
    """ Representation of Center """
    if models.storage_t == "db":
        __tablename__ = 'center'

        center_no = Column(String(5), primary_key=True)
        center_name = Column(String(50), nullable=False)
        is_open = Column(Boolean, nullable=False, default=False)
        __table_args__ = (UniqueConstraint('center_name', name='center_name_UNIQUE'),)
    else:
        subj_id = ""
        title = ""

    def __init__(self, *args, **kwargs):
        """ Center initialization """
        super().__init__(*args, **kwargs)
