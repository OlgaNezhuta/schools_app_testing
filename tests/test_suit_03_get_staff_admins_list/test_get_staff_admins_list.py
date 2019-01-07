import requests
import json
from config import *
from helpers.user_helpers import *
from tests.test_suit_03_get_staff_admins_list.get_staff_admins_list_test_data import *

GET_STAFF_ADMINS_LIST_URI = '/staff/admins'


def test_01_get_staff_admins_list_with_valid_token_and_pagination():
    url = BASE_URL + GET_STAFF_ADMINS_LIST_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    for el in payload:
        r = requests.get(url, params=el, headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


def test_02_get_staff_admins_list_with_unauthorized_user():
    url = BASE_URL + GET_STAFF_ADMINS_LIST_URI
    r = requests.get(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


