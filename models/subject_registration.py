#!/usr/bin/python
""" SubjectRegistration class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import uuid


class SubjectRegistration(BaseModel, Base):
    """Representation of SubjectRegistration """
    if models.storage_t == "db":
        __tablename__ = 'subject_registration'

        exam_reg = Column(String(50), ForeignKey('exam_registration.reg_id'), primary_key=True)
        exam_subj = Column(String(5), ForeignKey('exam_subject.code'), primary_key=True)

        exam_registration_rel = relationship("ExamRegistration")
        exam_subject_rel = relationship("ExamSubject")
    else:
        ses_id = ""
        year = ""

    def __init__(self, *args, **kwargs):
        """ SubjectRegistration initialization """
        super().__init__(*args, **kwargs)
