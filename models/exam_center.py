#!/usr/bin/python
""" ExamCenter class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
import uuid


class ExamCenter(BaseModel, Base):
    """ Representation of ExamCenter """
    if models.storage_t == "db":
        __tablename__ = 'exam_center'

        center = Column(String(5), ForeignKey('center.center_no'), primary_key=True)
        exam = Column(String(50), ForeignKey('exam.exam_id'), primary_key=True)
        is_open = Column(Boolean, nullable=False, default=False)

        center_rel = relationship("Center")
        exam_rel = relationship("Exam")
    else:
        ses_id = ""
        year = ""

    def __init__(self, *args, **kwargs):
        """ ExamCenter initialization """
        super().__init__(*args, **kwargs)
