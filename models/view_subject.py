#!/usr/bin/python
""" ViewSubject class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.types import TypeDecorator
import uuid

class ViewSubject(BaseModel, Base):
    """Representation of ViewSubject """
    if models.storage_t == "db":
        __tablename__ = 'view_subject'

        code = Column(String(5), primary_key=True)
        title = Column(String(50))
        exam = Column(String(50))
    else:
        ses_id = ""
        year = ""

    def __init__(self, *args, **kwargs):
        """ ViewSubject initialization """
        super().__init__(*args, **kwargs)
