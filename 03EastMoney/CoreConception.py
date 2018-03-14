from WebRequest import WebRequest
from time import sleep
import requests
import csv
import json

request = WebRequest()


def save_hxtc(js):
    if not js['hxtc']:
        return
    for i in js['hxtc']:
        with open('./data/CoreConception/hxtc.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            info = i.values()
            writer.writerow(info)
    return


def get_coreconception(code='sz000001'):
    base_url = 'http://emweb.securities.eastmoney.com/PC_HSF10/CoreConception/CoreConceptionAjax'
    response = request.get(base_url, params={'code': code})
    if response.status_code != 200:
        response = get_shareholders(code)
    return response.json()


js = get_coreconception()


if __name__ == '__main__':
    CSVfile = open('./data/code_list.csv', 'r')
    readCSV = csv.reader(CSVfile, delimiter=',')

    for row in readCSV:
        code = row[1]
        js = get_coreconception(code)
        save_hxtc(js)

    CSVfile.close()
