#!/usr/bin/python
""" holds class Exam"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, UniqueConstraint
import uuid


class Exam(BaseModel, Base):
    """Representation of exam """
    if models.storage_t == "db":
        __tablename__ = 'exam'

        exam_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
        exam_name = Column(String(50), nullable=False)
        exam_abbrev = Column(String(50), nullable=False)
        __table_args__ = (
            UniqueConstraint('exam_name', name='exam_name_UNIQUE'),
            UniqueConstraint('exam_abbrev', name='exam_abbrev_UNIQUE')
        )
    else:
        subj_id = ""
        title = ""

    def __init__(self, *args, **kwargs):
        """initializes exam"""
        super().__init__(*args, **kwargs)
