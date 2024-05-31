#!/usr/bin/python
""" holds class Candidate"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import uuid


class Candidate(BaseModel, Base):
    """Representation of candidate """
    if models.storage_t == "db":
        __tablename__ = 'candidate'

        gce_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
        first_name = Column(String(50), nullable=False)
        middle_name = Column(String(50), nullable=False)
        last_name = Column(String(50), nullable=False)
    else:
        ses_id = ""
        year = ""

    def __init__(self, *args, **kwargs):
        """initializes candidate"""
        super().__init__(*args, **kwargs)
