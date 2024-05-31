#!/usr/bin/python
""" holds class Center"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, UniqueConstraint


class Center(BaseModel, Base):
    """Representation of center """
    if models.storage_t == "db":
        __tablename__ = 'center'

        center_no = Column(String(5), primary_key=True)
        center_name = Column(String(50), nullable=False)
        __table_args__ = (UniqueConstraint('center_name', name='center_name_UNIQUE'),)
    else:
        subj_id = ""
        title = ""

    def __init__(self, *args, **kwargs):
        """initializes center"""
        super().__init__(*args, **kwargs)
