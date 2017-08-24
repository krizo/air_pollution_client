import os
import requests
import json

AQICN_TOKEN = os.environ.get('AQICN_TOKEN', None)
BASE_URL = "https://api.waqi.info/"

class AqicnApiClient:
    def __init__(self, token=AQICN_TOKEN):
        self.token = token
        self.base_url = BASE_URL

    def get_city(self, city):
        url = self.base_url + "feed/" + city + "/"
        return self._request(url)

    def search(self, keyword):
        url = self.base_url + "search/"
        params = { "keyword": keyword }
        return self._request(url, params)

    def _request(self, url, params={}):
        params['token'] = self.token
        response = requests.get(url, params=params)
        return self.handle_response(response)

    def handle_response(self, response):
        error_msg = 'Error on Aqicn api request.'
        content = response.json()
        if content['status'] == 'ok':
            return content['data']
        else:
            raise ApiException(content['data'], resource_url = response.url)


class ApiException(Exception):
    def __init__(self, msg, resource_url=None, status_code=None):
        self.msg = msg
        self.resource_url = resource_url
        self.status_code= status_code