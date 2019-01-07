import requests
import json
from config import *
from helpers.user_helpers import *

CHECK_STAFF_ADMIN_RIGHTS_BY_SELF_URI = '/staff/admins/rights/me'


def test_01_check_staff_admin_rights_by_self_with_valid_token():
    url = BASE_URL + CHECK_STAFF_ADMIN_RIGHTS_BY_SELF_URI
    token = login(STAFF_ADMIN_LOGIN_CREDS)
    r = requests.get(url, headers={"content-type": "application/json",
                                   "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_02_check_staff_admin_rights_by_self_with_unauthorized_user():
    url = BASE_URL + CHECK_STAFF_ADMIN_RIGHTS_BY_SELF_URI
    r = requests.get(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


def test_03_check_staff_admin_rights_by_self_with_wrong_role_school_admin():
    url = BASE_URL + CHECK_STAFF_ADMIN_RIGHTS_BY_SELF_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    r = requests.get(url, headers={"content-type": "application/json",
                                   "Authorization": token})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


def test_04_check_staff_admin_rights_by_self_with_wrong_role_guest_user():
    url = BASE_URL + CHECK_STAFF_ADMIN_RIGHTS_BY_SELF_URI
    token = guest_login(GUEST_USER_CREDS)
    r = requests.get(url, headers={"content-type": "application/json",
                                   "Authorization": token})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


