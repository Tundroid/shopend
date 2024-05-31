#!/usr/bin/python
""" holds class Session"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Boolean, UniqueConstraint
import uuid


class Session(BaseModel, Base):
    """Representation of session """
    if models.storage_t == "db":
        __tablename__ = 'session'

        ses_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
        year = Column(Integer, nullable=False)
        is_open = Column(Boolean, nullable=False, default=False)
        __table_args__ = (
            UniqueConstraint('year', name='year_UNIQUE'),
        )
    else:
        ses_id = ""
        year = ""

    def __init__(self, *args, **kwargs):
        """initializes session"""
        super().__init__(*args, **kwargs)
