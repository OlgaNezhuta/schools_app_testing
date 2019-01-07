import requests
import json
from config import *
from helpers.user_helpers import *
from tests.test_suit_01_create_staff_admin.create_staff_admin_test_data import *

CREATE_STAFF_ADMIN_URI = '/staff/admins'


def test_01_create_staff_admin_with_correct_creds():
    url = BASE_URL + CREATE_STAFF_ADMIN_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    for el in valid_creds:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


def test_02_create_staff_admin_with_incorrect_creds():
    url = BASE_URL + CREATE_STAFF_ADMIN_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    for el in invalid_creds:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == BAD_REQUEST_STATUS_CODE


def test_03_create_staff_admin_with_existing_creds():
    url = BASE_URL + CREATE_STAFF_ADMIN_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    r = requests.post(url, data=json.dumps(existing_creds), headers={"content-type": "application/json",
                                                                 "Authorization": token})
    print(r.status_code)
    assert r.status_code == BAD_REQUEST_STATUS_CODE

