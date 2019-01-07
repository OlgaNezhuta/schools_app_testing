import requests
import json
from config import *
from helpers.user_helpers import *

LOGOUT_STAFF_ADMIN_URI = '/users/auth'


def test_01_logout_with_valid_token():
    url = BASE_URL + LOGOUT_STAFF_ADMIN_URI
    token = login(STAFF_ADMIN_LOGIN_CREDS)
    r = requests.delete(url, headers={"Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_02_logout_with_incorrect_token():
    url = BASE_URL + LOGOUT_STAFF_ADMIN_URI
    token = "eyJhbGciOUzI1NiIR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltc" \
            "y9uYW1lIjoib2xnYS5uZXpodXRhLmNyQGdtYWlsLmNvbSIsImlzUmVmcmVzaCI6IkZhbHNlIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmc" \
            "vd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZWlkZW50aWZpZXIiOiIxMTk1IiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA" \
            "4LzA2L2lkZW50aXR5L2NsYWltcy9yb2xlIjoiVXNlciIsIm5iZiI6MTU0NjUxMzM4MywiZXhwIjoxNTQ3NzIyOTgzLCJpc3MiOiJOTFNBdXRoU2VydmVyIiwiYXVkIjoiQ" \
            "2xpZW50In0.OqQZPEiDtPMAlWbUjbcvsME-qs_htnPAXRHu4gc82mM"
    r = requests.delete(url, headers={"Authorization": token})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


def test_03_logout_with_invalid_token():
    url = BASE_URL + LOGOUT_STAFF_ADMIN_URI
    token = login(STAFF_ADMIN_LOGIN_CREDS)
    requests.delete(url, headers={"Authorization": token})
    r = requests.delete(url, headers={"Authorization": token})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE
