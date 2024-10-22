#!/usr/bin/python
""" RecordDetail class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import (
    Column, String, SmallInteger, Integer,
    Date, Text, TIMESTAMP, ForeignKey
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class RecordDetail(BaseModel, Base):
    """ Representation of Record Detail """
    if models.storage_t == "db":
        __tablename__ = 'record_detail'
        __table_args__ = {'schema': 'mole_commerce'}

        batch = Column(String(50), primary_key=True)
        operation = Column(SmallInteger,
                           ForeignKey('mole_commerce.operation.id'))
        receiver = Column(Integer,
                          ForeignKey('mole_commerce.client_account.id'))
        source_depot = Column(SmallInteger,
                              ForeignKey('mole_commerce.depot_detail.id'))
        dest_depot = Column(SmallInteger,
                            ForeignKey('mole_commerce.depot_detail.id'))
        rec_date = Column(Date, nullable=False)
        ref = Column(String(50), nullable=False)
        app_user = Column(SmallInteger,
                          ForeignKey('mole_commerce.user_account.id'))
        rec_desc = Column(Text)
        datetime = Column(TIMESTAMP, nullable=False,
                          server_default=func.current_timestamp())

        # Establish relationships
        operation_rel = relationship('Operation', backref='record_details')
        receiver_rel = relationship('ClientAccount', backref='record_details')
        source_depot_rel = relationship('DepotDetail',
                                        foreign_keys=[source_depot],
                                        backref='source_record_details')
        dest_depot_rel = relationship('DepotDetail',
                                      foreign_keys=[dest_depot],
                                      backref='dest_record_details')
        app_user_rel = relationship('UserAccount', backref='record_details')

    def __init__(self, *args, **kwargs):
        """ RecordDetail initialization """
        super().__init__(*args, **kwargs)
