# ~/tests/test_robot.py

import pytest
import requests
from routes import RobotApi, RobotsApi

base_url = "http://localhost:8080/api"
headers = {'Content-Type': 'application/json' }

def test_get_all_robot():
    url = base_url + "/robot"
    response = requests.get(url, headers=headers)

    # Then
    assert response.status_code == 200

def test_create_robot():
    url = base_url + "/robot"
    response = requests.post(url, data={}, headers=headers)

    assert response.status_code == 201

def test_get_robot():
    id = 1
    url = base_url + "/robot/" + str(id)
    response = requests.get(url, headers=headers)

    assert response.status_code == 200

def test_update_robot():
    id = 1
    url = base_url + "/robot/" + str(id)
    response = requests.put(url, data={},headers=headers)

    assert response.status_code == 202

def test_delete_robot():
    id = 1
    url = base_url + "/robot/" + str(id)
    response = requests.delete(url, headers=headers)

    assert response.status_code == 204