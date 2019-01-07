import requests
import json
from config import *
from helpers.user_helpers import *

VIEW_CONTACT_URI = '/contacts/490'


def test_01_view_contact_with_valid_token():
    url = BASE_URL + VIEW_CONTACT_URI
    token = guest_login(GUEST_USER_CREDS)
    r = requests.post(url, headers={"content-type": "application/json",
                                    "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_02_view_contact_with_unauthorized_user():
    url = BASE_URL + VIEW_CONTACT_URI
    r = requests.post(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


def test_03_view_contact_with_wrong_role():
    url = BASE_URL + VIEW_CONTACT_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    r = requests.post(url, headers={"content-type": "application/json",
                                   "Authorization": token})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


def test_04_view_contact_with_wrong_staff_admin_id():
    url = BASE_URL + '/contacts/345'
    token = guest_login(GUEST_USER_CREDS)
    r = requests.post(url, headers={"content-type": "application/json",
                                   "Authorization": token})
    print(r.status_code)
    assert r.status_code == NOT_FOUND_STATUS_CODE
