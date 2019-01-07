import requests
import json
from config import *
from helpers.user_helpers import *
from data_generators.external_links_generator.external_links_test_data import *

CREATE_EXTERNAL_LINK_URI = '/links'
BASE_URL = 'https://api.school-app.dev.cleveroad.com/api/v2'


def external_links_generator():
    url = BASE_URL + CREATE_EXTERNAL_LINK_URI
    token = login(SCHOOL_ADMIN_LOGIN_CREDS)
    for el in external_links:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


new_external_links = external_links_generator()

