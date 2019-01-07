import requests
import json
from config import *
from helpers.user_helpers import *
from tests.test_suit_05_edit_staff_admin_info.edit_staff_admin_info_test_data import *

EDIT_STAFF_ADMIN_INFO_URI = '/staff/admins/490'


def test_01_edit_staff_admin_info_with_correct_creds():
    url = BASE_URL + EDIT_STAFF_ADMIN_INFO_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    for el in valid_creds:
        r = requests.put(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


def test_02_edit_staff_admin_info_with_incorrect_creds():
    url = BASE_URL + EDIT_STAFF_ADMIN_INFO_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    for el in invalid_creds:
        r = requests.put(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == BAD_REQUEST_STATUS_CODE


def test_03_edit_staff_admin_info_with_unauthorized_user():
    url = BASE_URL + EDIT_STAFF_ADMIN_INFO_URI
    r = requests.put(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE




