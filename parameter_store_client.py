import requests
import os
from urllib.parse import urlencode

class ParameterStoreClient: 
    def __init__(self):
        self.url_base = 'http://localhost:2773/systemsmanager/parameters/get/'
    
    def get_parameter(self, path):
        url = self.url_base + '?name=' + urlencode(path)
        headers = {
            'X-Aws-Parameters-Secrets-Token': os.environ['AWS_SESSION_TOKEN']
        }
        res = requests.get(url, headers=headers)
        print(res)
    