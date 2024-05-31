#!/usr/bin/python
""" Subject class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, UniqueConstraint
import uuid


class Subject(BaseModel, Base):
    """ Representation of Subject """
    if models.storage_t == "db":
        __tablename__ = 'subject'

        subj_id = Column(String(50), primary_key=True, default=lambda: str(uuid.uuid4()))
        title = Column(String(50), nullable=False)
        __table_args__ = (
            UniqueConstraint('title', name='title_UNIQUE'),
        )
    else:
        subj_id = ""
        title = ""

    def __init__(self, *args, **kwargs):
        """ Subject initialization """
        super().__init__(*args, **kwargs)
