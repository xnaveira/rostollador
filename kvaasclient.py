import base64
import logging
import os

import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

"""
http://keyvalue.immanuel.co client
"""
class Kvaas:
    def __init__(self):
        self.base_url = 'http://keyvalue.immanuel.co'
        self.api_key = os.getenv('KEY_VALUE')

    def _b64e(self,str):
        return base64.b64encode(str.encode('latin-1')).decode('ascii')

    def _b64d(self,str):
        return base64.b64decode(str.encode('ascii')).decode('latin-1')

    def setValue(self, key, value):
        post_string = '{}/api/KeyVal/UpdateValue/{}/{}/{}'.format(self.base_url, self.api_key, self._b64e(key), self._b64e(value))
        logging.debug('Post: {}'.format(post_string))
        r = requests.post(post_string)
        if r.status_code != '200':
            logging.error('Couldn''t post to key/value store')


    def getValue(self,key):
        get_string = '{}/api/KeyVal/GetValue/{}/{}'.format(self.base_url, self.api_key, self._b64e(key))
        logging.debug('Get: {}'.format(get_string))
        r = requests.get(get_string)
        if r.status_code != 200:
            logging.error('Couldn''t retrieve from key/value store')
            return ''
        else:
            return self._b64d(r.text)
