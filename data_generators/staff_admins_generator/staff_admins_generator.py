import requests
import json
from config import *
from helpers.user_helpers import *
from data_generators.staff_admins_generator.staff_admins_test_data import *

CREATE_STAFF_ADMIN_URI = '/staff/admins'


def staff_admins_generator():
    url = BASE_URL + CREATE_STAFF_ADMIN_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    for el in staff_admins:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


new_staff_admins = staff_admins_generator()



