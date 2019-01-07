import requests
import json
from config import *
from helpers.user_helpers import *
from data_generators.notifications_categories_generator.notifications_categories_test_data import *

CREATE_NOTIFICATIONS_CATEGORY_URI = '/notifications/categories'


def notifications_categories_generator():
    url = BASE_URL + CREATE_NOTIFICATIONS_CATEGORY_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    for el in notifications_categories:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


new_notifications_categories= notifications_categories_generator()


