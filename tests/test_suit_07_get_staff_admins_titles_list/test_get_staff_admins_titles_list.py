import requests
import json
from config import *
from helpers.user_helpers import *

GET_STAFF_ADMINS_TITLES_LIST_URI = '/staff/admins/titles'


def test_01_get_staff_admins_titles_list_with_valid_token():
    url = BASE_URL + GET_STAFF_ADMINS_TITLES_LIST_URI
    token = guest_login(GUEST_USER_CREDS)
    r = requests.get(url, headers={"content-type": "application/json",
                                   "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_02_get_staff_admins_titles_list_with_unauthorized_user():
    url = BASE_URL + GET_STAFF_ADMINS_TITLES_LIST_URI
    r = requests.get(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


def test_03_get_staff_admins_titles_list_with_wrong_role():
    url = BASE_URL + GET_STAFF_ADMINS_TITLES_LIST_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    r = requests.get(url, headers={"content-type": "application/json",
                                   "Authorization": token})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE

