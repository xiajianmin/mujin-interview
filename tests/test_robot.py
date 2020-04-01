# ~/tests/test_robot.py

import pytest
from routes import RobotApi, RobotsApi

from app import db

def mydb():
    db.drop_all()
    db.create_all()

def test_create_robot():
    return

def test_get_all_robot():
    # When
    response = ''#RobotsApi.post('/api/robot', headers={"Content-Type": "application/json"})

    # Then
    assert response.status_code == 201

def test_get_robot():
    pass

def test_update_robot():
    pass

def test_delete_robot():
    pass