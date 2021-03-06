from WebRequest import WebRequest
from time import sleep
import requests
import csv
import json

request = WebRequest()


def save_RptManagerList(js, code='sz300365'):
    if not js['Result']['RptManagerList']:
        return
    code = code[2:]
    for i in js['Result']['RptManagerList']:
        i['code'] = code
        with open('./data/CompanyManagement/RptManagerList.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            info = i.values()
            writer.writerow(info)
    return


def save_RptShareHeldChangeList(js, code='sz300365'):
    if not js['Result']['RptShareHeldChangeList']:
        return
    code = code[2:]
    for i in js['Result']['RptShareHeldChangeList']:
        i['code'] = code
        with open('./data/CompanyManagement/RptShareHeldChangeList.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            info = i.values()
            writer.writerow(info)
    return


def get_companymanagement(code='sz300365'):
    base_url = 'http://emweb.securities.eastmoney.com/PC_HSF10/CompanyManagement/CompanyManagementAjax'
    response = request.get(base_url, params={'code': code})
    if response.status_code != 200:
        response = get_shareholders(code)
    return response.json()



if __name__ == '__main__':
    CSVfile = open('./data/code_list.csv', 'r')
    readCSV = csv.reader(CSVfile, delimiter=',')

    for row in readCSV:
        code = row[1]
        js = get_companymanagement(code)
        save_RptManagerList(js, code)
        save_RptShareHeldChangeList(js, code)

    CSVfile.close()
