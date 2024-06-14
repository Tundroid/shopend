#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.base_model import BaseModel, Base
from models.exam import Exam
from models.candidate import Candidate
from models.session import Session
from models.subject import Subject
from models.center import Center
from models.exam_subject import ExamSubject
from models.exam_session import ExamSession
from models.exam_center import ExamCenter
from models.admin import Admin
from models.exam_registration import ExamRegistration
from models.subject_registration import SubjectRegistration
from models.view_exam_registration import ViewExamRegistration
from models.view_subject_registration import ViewSubjectRegistration
from models.view_subject import ViewSubject
from models.admin_session import AdminSession
from models.candidate_session import CandidateSession
from os import getenv
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Session": Session, "Subject": Subject, "Exam": Exam, "Center": Center,
           "Candidate": Candidate, "ExamCenter": ExamCenter, "ExamSession": ExamSession,
           "ExamSubject": ExamSubject, "ExamRegistration": ExamRegistration,
           "SubjectRegistration": SubjectRegistration, "Admin": Admin,
           "ViewExamRegistration": ViewExamRegistration,
           "ViewSubjectRegistration": ViewSubjectRegistration,
           "ViewSubject": ViewSubject,
           "AdminSession": AdminSession,
           "CandidateSession": CandidateSession}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        CGCEB_MYSQL_USER = getenv('CGCEB_MYSQL_USER')
        CGCEB_MYSQL_PWD = getenv('CGCEB_MYSQL_PWD')
        CGCEB_MYSQL_HOST = getenv('CGCEB_MYSQL_HOST')
        CGCEB_MYSQL_DB = getenv('CGCEB_MYSQL_DB')
        CGCEB_ENV = getenv('CGCEB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(CGCEB_MYSQL_USER,
                                             CGCEB_MYSQL_PWD,
                                             CGCEB_MYSQL_HOST,
                                             CGCEB_MYSQL_DB))
        if CGCEB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None, cond=None):
        """query on the current database session"""
        new_dict = {}
        class_dict = classes.copy()
        if cls:
            class_dict = {cls.__class__.__name__: cls}
        for my_class in class_dict.values():
            if not cond:
                objs = self.__session.query(my_class).all()
            else:
                objs = self.__session.query(my_class).filter(eval(cond)).all()
            for obj in objs:
                obj_id = eval(f"obj.{inspect(my_class).primary_key[0].name}")
                key = f"{obj.__class__.__name__}.{obj_id}"
                new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        # Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            obj_id = eval(f"value.{inspect(cls).primary_key[0].name}")
            if (obj_id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
