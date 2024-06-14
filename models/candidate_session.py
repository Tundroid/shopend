#!/usr/bin/python
""" Candidate class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship
import uuid
import datetime


class CandidateSession(BaseModel, Base):
    """ Representation of Candidate """
    if models.storage_t == "db":
        __tablename__ = 'candidate_session'

        id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
        candidate = Column(String(50), ForeignKey('candidate.gce_id'), nullable=False)
        created = Column(DateTime, default=datetime.datetime.utcnow)
        expiry = Column(DateTime, default=datetime.datetime.utcnow)
        last_update = Column(DateTime, default=datetime.datetime.utcnow)
        
        candidate_rel = relationship("Candidate")
    else:
        ses_id = ""
        year = ""

    def __init__(self, *args, **kwargs):
        """ Candidate initialization """
        super().__init__(*args, **kwargs)
