# ~/tests/test_geometry.py

import pytest
import requests
from routes import GeometryApi, GeometriesApi

base_url = "http://localhost:8080/api"
headers = {'Content-Type': 'application/json' }

def test_get_all_geometry():
    robotid = 1
    linkid = 1
    url = base_url + "/robot/" + str(robotid) + "/link/" + str(linkid) + "/geometry"
    response = requests.get(url, headers=headers)

    # Then
    assert response.status_code == 200

def test_create_geometry():
    robotid = 1
    linkid = 1
    url = base_url + "/robot/" + str(robotid) + "/link/" + str(linkid) + "/geometry"
    response = requests.post(url, data={}, headers=headers)

    # Then
    assert response.status_code == 201

def test_get_geometry():
    robotid = 1
    linkid = 1
    geometryid = 1
    url = base_url + "/robot/" + str(robotid) + "/link/" + str(linkid) + "/geometry/" + str(geometryid)
    response = requests.get(url, headers=headers)

    # Then
    assert response.status_code == 200

def test_update_geometry():
    robotid = 1
    linkid = 1
    geometryid = 1
    url = base_url + "/robot/" + str(robotid) + "/link/" + str(linkid) + "/geometry/" + str(geometryid)
    response = requests.put(url, data={}, headers=headers)

    # Then
    assert response.status_code == 202

def test_delete_geometry():
    robotid = 1
    linkid = 1
    geometryid = 1
    url = base_url + "/robot/" + str(robotid) + "/link/" + str(linkid) + "/geometry/" + str(geometryid)
    response = requests.delete(url, headers=headers)

    # Then
    assert response.status_code == 204
