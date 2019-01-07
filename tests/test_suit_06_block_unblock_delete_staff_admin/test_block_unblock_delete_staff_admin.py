import requests
import json
from config import *
from helpers.user_helpers import *

BLOCK_UNBLOCK_STAFF_ADMIN_URI = '/staff/admins/490'


def test_01_block_staff_admin():
    url = BASE_URL + BLOCK_UNBLOCK_STAFF_ADMIN_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    r = requests.patch(url, data=json.dumps({"isBlock": True}), headers={"content-type": "application/json",
                                                                 "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE
    url = BASE_URL + LOGIN_URI
    r = requests.post(url, data=json.dumps(STAFF_ADMIN_LOGIN_CREDS), headers={'content-type': 'application/json'})
    print(r.status_code)
    assert r.status_code == FORBIDDEN_STATUS_CODE


def test_02_unblock_staff_admin():
    url = BASE_URL + BLOCK_UNBLOCK_STAFF_ADMIN_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    r = requests.patch(url, data=json.dumps({"isUnblock": True}), headers={"content-type": "application/json",
                                                                 "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE
    url = BASE_URL + LOGIN_URI
    r = requests.post(url, data=json.dumps(STAFF_ADMIN_LOGIN_CREDS), headers={'content-type': 'application/json'})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_03_delete_staff_admin():
    staff_admin_id = create_staff_admin_and_get_id()
    url = BASE_URL + '/staff/admins/' + str(staff_admin_id)
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    r = requests.patch(url, data=json.dumps({"isDelete": True}), headers={"content-type": "application/json",
                                                                 "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE
    url = BASE_URL + LOGIN_URI
    r = requests.post(url, data=json.dumps({"email": "olga999@example.com",
                                            "password": "qwerty1"
                                            }), headers={'content-type': 'application/json'})
    print(r.status_code)
    assert r.status_code == NOT_FOUND_STATUS_CODE


def test_04_block_staff_admin_with_unauthorized_user():
    url = BASE_URL + BLOCK_UNBLOCK_STAFF_ADMIN_URI
    r = requests.patch(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


