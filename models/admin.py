#!/usr/bin/python
""" Admin class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
import uuid


class Admin(BaseModel, Base):
    """ Representation of Admin """
    if models.storage_t == "db":
        __tablename__ = 'admin'

        admin_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
        name = Column(String(50), nullable=False)
        center = Column(String(5), ForeignKey('center.center_no'))
        __table_args__ = (
            UniqueConstraint('name', name='name_UNIQUE'),
        )
        center_rel = relationship("Center")
    else:
        ses_id = ""
        year = ""

    def __init__(self, *args, **kwargs):
        """ Admin initialization """
        super().__init__(*args, **kwargs)
