import requests
import json
from config import *
from helpers.user_helpers import *
from data_generators.notifications_history_generator.notifications_history_test_data import *

CREATE_NOTIFICATIONS_URI = '/notifications'


def notifications_generator():
    url = BASE_URL + CREATE_NOTIFICATIONS_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    for el in notifications:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


new_notifications= notifications_generator()


