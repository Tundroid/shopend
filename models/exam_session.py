#!/usr/bin/python
""" ExamSession class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, Boolean
from sqlalchemy.orm import relationship
import uuid


class ExamSession(BaseModel, Base):
    """ Representation of ExamSession """
    if models.storage_t == "db":
        __tablename__ = 'exam_session'

        id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
        session = Column(String(50), nullable=False)
        exam = Column(String(50), ForeignKey('exam.exam_id'), nullable=False)
        is_open = Column(Boolean, nullable=False, default=False)
        __table_args__ = (
            UniqueConstraint('session', name='session_UNIQUE'),
        )

        exam_rel = relationship("Exam")
    else:
        ses_id = ""
        year = ""

    def __init__(self, *args, **kwargs):
        """ ExamSession initialization """
        super().__init__(*args, **kwargs)
