import requests
import json
from config import *


LOGIN_URI = '/users/auth'
SCHOOL_ADMIN_LOGIN_CREDS = {"email": "olga.nezhuta@gmail.com",
               "password": "qwerty123"}
STAFF_ADMIN_LOGIN_CREDS = {"email": "olga.nezhuta.cr@gmail.com",
               "password": "qwerty1"}
LOGOUT_URI = '/users/auth'
CREATE_STAFF_ADMIN_URI = '/staff/admins'
GUEST_LOGIN_URI = '/users/guests'
GUEST_USER_CREDS = {"guestToken": "string",
                    "schoolId": 64,
                    "role": 3}


def login(creds):
    url = BASE_URL + LOGIN_URI
    r = requests.post(url, data=json.dumps(creds), headers=BASE_HEADERS)
    assert r.status_code == SUCCESS_STATUS_CODE
    my_token = r.json()['data']['access']['token']
    return 'Bearer {}'.format(my_token)


def refresh_token(creds):
    url = BASE_URL + LOGIN_URI
    r = requests.post(url, data=json.dumps(creds), headers=BASE_HEADERS)
    assert r.status_code == SUCCESS_STATUS_CODE
    my_refresh_token = r.json()['data']['access']['refreshToken']
    return my_refresh_token


def create_staff_admin_and_get_id():
    url = BASE_URL + CREATE_STAFF_ADMIN_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    staff_creds = {"email": "olga999@example.com",
                   "firstName": "olga",
                   "lastName": "staff",
                   "title": "test"
                   }
    r = requests.post(url, data=json.dumps(staff_creds), headers={"content-type": "application/json",
                                                                 "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE
    my_id = r.json()['data']['id']
    return my_id


def guest_login(creds):
    url = BASE_URL + GUEST_LOGIN_URI
    r = requests.post(url, data=json.dumps(creds), headers=BASE_HEADERS)
    assert r.status_code == SUCCESS_STATUS_CODE
    my_token = r.json()['data']['access']['token']
    return 'Bearer {}'.format(my_token)


def logout(token):
    url = BASE_URL + LOGOUT_URI
    headers = BASE_HEADERS
    headers.update({'Authorization': token})
    print(headers)
    r = requests.delete(url, headers=headers)
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE
