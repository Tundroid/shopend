from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, UniqueConstraint, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Candidate(Base):
    __tablename__ = 'candidate'

    gce_id = Column(String(50), primary_key=True, default='UUID()')
    first_name = Column(String(50), nullable=False)
    middle_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

class Center(Base):
    __tablename__ = 'center'

    center_no = Column(String(5), primary_key=True)
    center_name = Column(String(50), nullable=False)
    __table_args__ = (UniqueConstraint('center_name', name='center_name_UNIQUE'),)

class Exam(Base):
    __tablename__ = 'exam'

    exam_id = Column(String(50), primary_key=True, default='UUID()')
    exam_name = Column(String(50), nullable=False)
    exam_abbrev = Column(String(50), nullable=False)
    __table_args__ = (
        UniqueConstraint('exam_name', name='exam_name_UNIQUE'),
        UniqueConstraint('exam_abbrev', name='exam_abbrev_UNIQUE')
    )

class ExamCenter(Base):
    __tablename__ = 'exam_center'

    center = Column(String(5), ForeignKey('center.center_no'), primary_key=True)
    exam = Column(String(50), ForeignKey('exam.exam_id'), primary_key=True)

    center_rel = relationship("Center")
    exam_rel = relationship("Exam")

class ExamRegistration(Base):
    __tablename__ = 'exam_registration'

    reg_id = Column(String(50), primary_key=True, default='UUID()')
    candidate = Column(String(50), ForeignKey('candidate.gce_id'), nullable=False)
    center = Column(String(5), ForeignKey('center.center_no'), nullable=False)
    exam_session = Column(String(50), ForeignKey('exam_session.id'), nullable=False)
    can_no = Column(Integer, nullable=False, server_default='0')
    is_complete = Column(Boolean, nullable=False, default=False)

    candidate_rel = relationship("Candidate")
    center_rel = relationship("Center")
    exam_session_rel = relationship("ExamSession")

class ExamSession(Base):
    __tablename__ = 'exam_session'

    id = Column(String(50), primary_key=True, default='UUID()')
    session = Column(String(50), nullable=False)
    exam = Column(String(50), ForeignKey('exam.exam_id'), nullable=False)
    __table_args__ = (
        UniqueConstraint('session', name='session_UNIQUE'),
    )

    exam_rel = relationship("Exam")

class ExamSubject(Base):
    __tablename__ = 'exam_subject'

    code = Column(String(5), primary_key=True)
    subject = Column(String(50), ForeignKey('subject.subj_id'), nullable=False)
    exam = Column(String(50), ForeignKey('exam.exam_id'), nullable=False)

    subject_rel = relationship("Subject")
    exam_rel = relationship("Exam")

class SubjectRegistration(Base):
    __tablename__ = 'subject_registration'

    exam_reg = Column(String(50), ForeignKey('exam_registration.reg_id'), primary_key=True)
    exam_subj = Column(String(5), ForeignKey('exam_subject.code'), primary_key=True)

    exam_registration_rel = relationship("ExamRegistration")
    exam_subject_rel = relationship("ExamSubject")
