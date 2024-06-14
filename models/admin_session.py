#!/usr/bin/python
""" Admin class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship
import uuid
import datetime


class AdminSession(BaseModel, Base):
    """ Representation of Admin """
    if models.storage_t == "db":
        __tablename__ = 'admin_session'

        id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
        admin = Column(String(50), ForeignKey('admin.admin_id'), nullable=False)
        created = Column(DateTime, default=datetime.datetime.utcnow())
        expiry = Column(DateTime, default=datetime.datetime.utcnow())
        last_update = Column(DateTime, default=datetime.datetime.utcnow())
        
        admin_rel = relationship("Admin")
    else:
        ses_id = ""
        year = ""

    def __init__(self, *args, **kwargs):
        """ Admin initialization """
        super().__init__(*args, **kwargs)

    def expired(self):
        if (self.expiry > datetime.datetime.utcnow()):
            self.expiry = datetime.datetime.utcnow()
            self.save()
            return False
        return True