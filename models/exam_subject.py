#!/usr/bin/python
""" ExamSubject class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid


class ExamSubject(BaseModel, Base):
    """ Representation of ExamSubject """
    if models.storage_t == "db":
        __tablename__ = 'exam_subject'

        code = Column(String(5), primary_key=True)
        subject = Column(String(50), ForeignKey('subject.subj_id'), nullable=False)
        exam = Column(String(50), ForeignKey('exam.exam_id'), nullable=False)

        subject_rel = relationship("Subject")
        exam_rel = relationship("Exam")
    else:
        ses_id = ""
        year = ""

    def __init__(self, *args, **kwargs):
        """ ExamSubject initialization """
        super().__init__(*args, **kwargs)
