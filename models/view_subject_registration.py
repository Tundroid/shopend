#!/usr/bin/python
""" ExamRegistration class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.types import TypeDecorator
import uuid

class MySQLBit(TypeDecorator):
    impl = Integer

    def process_result_value(self, value, dialect):
        return value == b'\x01'

class ViewSubjectRegistration(BaseModel, Base):
    """Representation of ViewSubjectRegistration """
    if models.storage_t == "db":
        __tablename__ = 'view_subject_registration'

        row_num = Column(Integer, primary_key=True)
        reg = Column(String(50))
        code = Column(String(50))
        title = Column(String(50))
        subject_fee = Column(Integer)
        practical_fee = Column(Integer)
        has_practical = Column(MySQLBit)
    else:
        ses_id = ""
        year = ""

    def __init__(self, *args, **kwargs):
        """ ViewSubjectRegistration initialization """
        super().__init__(*args, **kwargs)
