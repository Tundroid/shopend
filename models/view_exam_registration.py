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

class ViewExamRegistration(BaseModel, Base):
    """Representation of ViewExamRegistration """
    if models.storage_t == "db":
        __tablename__ = 'view_exam_registration'

        reg_id = Column(String(50), primary_key=True)
        candidate = Column(String(50))
        exam_name = Column(String(5))
        exam_abbrev = Column(String(50))
        year = Column(Integer)
        is_complete = Column(MySQLBit)
        is_exam_center_open = Column(MySQLBit)
        is_center_open = Column(MySQLBit)
        is_exam_session_open = Column(MySQLBit)
        is_session_open = Column(MySQLBit)
    else:
        ses_id = ""
        year = ""

    def __init__(self, *args, **kwargs):
        """ ViewExamRegistration initialization """
        super().__init__(*args, **kwargs)
