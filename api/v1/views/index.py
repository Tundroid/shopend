#!/usr/bin/python3
"""API main routes"""

from flask import jsonify

from api.v1.views import app_views
from models import storage
from models.exam import Exam
from models.candidate import Candidate
from models.session import Session
from models.subject import Subject
from models.center import Center
from models.admin import Admin
from models.exam_subject import ExamSubject
from models.exam_session import ExamSession
from models.exam_center import ExamCenter
from models.exam_registration import ExamRegistration
from models.subject_registration import SubjectRegistration

classes = {"Session": Session, "Subject": Subject, "Exam": Exam, "Center": Center,
           "Candidate": Candidate, "ExamCenter": ExamCenter, "ExamSession": ExamSession,
           "ExamSubject": ExamSubject, "ExamRegistration": ExamRegistration,
           "SubjectRegistration": SubjectRegistration, "Admin": Admin}


@app_views.route("/status", strict_slashes=False)
def status():
    """Returns the status in JSON format"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def stats():
    """Endpoint that retrieves the number of each objects by type"""
    stats_dict = {}
    for cls_name, cls in classes.items():
        stats_dict[cls_name] = storage.count(cls)
    return jsonify(stats_dict)
