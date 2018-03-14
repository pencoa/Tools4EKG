from WebRequest import WebRequest
from time import sleep
import requests
import csv
import json

request = WebRequest()


def save_jbzl(js, code='sz000001'):
    if not js['Result']['jbzl']:
        return
    code = code[2:]
    js['Result']['jbzl']['code'] = code
    with open('./data/CompanySurvey/jbzl.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        info = js['Result']['jbzl'].values()
        writer.writerow(info)
    return


def save_fxxg(js, code='sz000001'):
    if not js['Result']['fxxg']:
        return
    code = code[2:]
    js['Result']['fxxg']['code'] = code
    with open('./data/CompanySurvey/fxxg.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        info = js['Result']['fxxg'].values()
        writer.writerow(info)
    return


def get_companysurvey(code='sz000001'):
    base_url = 'http://emweb.securities.eastmoney.com/PC_HSF10/CompanySurvey/CompanySurveyAjax'
    response = request.get(base_url, params={'code': code})
    if response.status_code != 200:
        response = get_shareholders(code)
    return response.json()


js = get_companysurvey()


if __name__ == '__main__':
    CSVfile = open('./data/code_list.csv', 'r')
    readCSV = csv.reader(CSVfile, delimiter=',')

    for row in readCSV:
        code = row[1]
        js = get_companysurvey(code)
        save_jbzl(js, code)
        save_fxxg(js, code)

    CSVfile.close()
