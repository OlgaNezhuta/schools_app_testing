import requests
import json
from config import *
from helpers.user_helpers import *

GET_STAFF_ADMINS_LIST_BY_TITLE_URI = '/staff/admins/app'


def test_01_get_staff_admins_list_by_title_with_valid_creds():
    url = BASE_URL + GET_STAFF_ADMINS_LIST_BY_TITLE_URI
    token = guest_login(GUEST_USER_CREDS)
    r = requests.get(url, params={"title": "test"}, headers={"content-type": "application/json",
                                   "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_01_get_staff_admins_list_by_title_with_invalid_creds():
    url = BASE_URL + GET_STAFF_ADMINS_LIST_BY_TITLE_URI
    token = guest_login(GUEST_USER_CREDS)
    r = requests.get(url, params={"title": "qwertyqwerty"}, headers={"content-type": "application/json",
                                                                     "Authorization": token})
    print(r.status_code)
    assert r.status_code == NOT_FOUND_STATUS_CODE


def test_03_get_staff_admins_list_by_title_with_unauthorized_user():
    url = BASE_URL + GET_STAFF_ADMINS_LIST_BY_TITLE_URI
    r = requests.get(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


def test_04_get_staff_admins_list_by_title_with_wrong_role():
    url = BASE_URL + GET_STAFF_ADMINS_LIST_BY_TITLE_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    r = requests.get(url, headers={"content-type": "application/json",
                                   "Authorization": token})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE





