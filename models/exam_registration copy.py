#!/usr/bin/python
""" ExamRegistration class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship
import uuid


class ExamRegistration(BaseModel, Base):
    """Representation of ExamRegistration """
    if models.storage_t == "db":
        __tablename__ = 'exam_registration'

        reg_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
        candidate = Column(String(50), ForeignKey('candidate.gce_id'), nullable=False)
        center = Column(String(5), ForeignKey('center.center_no'), nullable=False)
        exam_session = Column(String(50), ForeignKey('exam_session.id'), nullable=False)
        can_no = Column(Integer, nullable=False, server_default='0')
        is_complete = Column(Boolean, nullable=False, default=False)

        candidate_rel = relationship("Candidate")
        center_rel = relationship("Center")
        exam_session_rel = relationship("ExamSession")
    else:
        ses_id = ""
        year = ""

    def __init__(self, *args, **kwargs):
        """ ExamRegistration initialization """
        super().__init__(*args, **kwargs)
