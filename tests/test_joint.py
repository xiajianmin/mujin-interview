# ~/tests/test_joint.py

import pytest
import requests
from routes import JointApi, JointsApi

base_url = "http://localhost:8080/api"
headers = {'Content-Type': 'application/json' }

def test_get_all_joints():
    robotid = 1
    url = base_url + "/robot/" + str(robotid) + "/joint"
    response = requests.get(url, headers=headers)

    # Then
    assert response.status_code == 200

def test_get_joint():
    robotid = 1
    jointid = 2
    url = base_url + "/robot/" + str(robotid) + "/joint/" + str(jointid)
    response = requests.get(url, headers=headers)

    # Then
    assert response.status_code == 200

def test_update_joint():
    robotid = 1
    jointid = 2
    url = base_url + "/robot/" + str(robotid) + "/joint/" + str(jointid)
    response = requests.put(url, headers=headers)

    # Then
    assert response.status_code == 202