import requests
import json
from config import *
from helpers.user_helpers import *
from data_generators.events_generator.events_test_data import *

CREATE_EVENT_URI = '/events'
BASE_URL = 'https://api.school-app.dev.cleveroad.com/api/v2'


def events_generator():
    url = BASE_URL + CREATE_EVENT_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    for el in events:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


new_events = events_generator()



