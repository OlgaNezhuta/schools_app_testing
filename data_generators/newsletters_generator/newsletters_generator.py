import requests
import json
from config import *
from helpers.user_helpers import *
from data_generators.newsletters_generator.newsletters_test_data import *

CREATE_NEWSLETTER_URI = '/newsletters'


def newsletters_generator():
    url = BASE_URL + CREATE_NEWSLETTER_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    for el in newsletters:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


new_newsletters = newsletters_generator()


