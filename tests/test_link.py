# ~/tests/test_link.py

import pytest
import requests
from routes import LinkApi, LinksApi

base_url = "http://localhost:8080/api"
headers = {'Content-Type': 'application/json' }

def test_get_all_links():
    robotid = 1
    url = base_url + "/robot/" + str(robotid) + "/link"
    # Additional headers.
    response = requests.get(url, headers=headers)

    # Then
    assert response.status_code == 200

def test_create_link():
    robotid = 1
    url = base_url + "/robot/" + str(robotid) + "/link"
    # Additional headers.
    response = requests.post(url, data={}, headers=headers)

    # Then
    assert response.status_code == 201

def test_get_link():
    robotid = 1
    linkid = 1
    url = base_url + "/robot/" + str(robotid) + "/link/" + str(linkid)
    response = requests.get(url, headers=headers)

    # Then
    assert response.status_code == 200

def test_update_link():
    robotid = 1
    linkid = 1
    url = base_url + "/robot/" + str(robotid) + "/link/" + str(linkid)
    response = requests.put(url, data={}, headers=headers)

    # Then
    assert response.status_code == 202

def test_delete_link():
    robotid = 1
    linkid = 1
    url = base_url + "/robot/" + str(robotid) + "/link/" + str(linkid)
    response = requests.delete(url, headers=headers)

    # Then
    assert response.status_code == 204
