import requests
import json
from config import *
from helpers.user_helpers import *
from tests.test_suit_04_change_staff_admin_rights.change_staff_admin_rights_test_data import *

CHANGE_STAFF_ADMIN_RIGHTS_URI = '/staff/admins/490/rights'


def test_01_change_staff_admin_rights_with_valid_creds():
    url = BASE_URL + CHANGE_STAFF_ADMIN_RIGHTS_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    for el in valid_creds:
        r = requests.patch(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


def test_02_change_staff_admin_rights_with_invalid_creds():
    url = BASE_URL + CHANGE_STAFF_ADMIN_RIGHTS_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    for el in invalid_creds:
        r = requests.patch(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == BAD_REQUEST_STATUS_CODE


def test_03_change_staff_admin_rights_with_unauthorized_user():
    url = BASE_URL + CHANGE_STAFF_ADMIN_RIGHTS_URI
    r = requests.patch(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE

