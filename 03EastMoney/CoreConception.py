from WebRequest import WebRequest
from time import sleep
import requests
import csv
import json

request = WebRequest()




def get_coreconception(code='sz000001'):
    base_url = 'http://emweb.securities.eastmoney.com/PC_HSF10/CoreConception/CoreConceptionAjax'
    response = request.get(base_url, params={'code': code})
    if response.status_code != 200:
        response = get_shareholders(code)
    return response.json()


js = get_coreconception()
