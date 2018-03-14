from WebRequest import WebRequest
from time import sleep
import requests
import csv
import json

request = WebRequest()

def write_zcfzb(js, code='sz300365'):
    if not js:
        return
    with open('./data/NewFinanceAnalysis/zcfzb.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        info = js[0].keys()
        writer.writerow(info)
    return

def save_zcfzb(js, code='sz300365'):
    if not js:
        return
    code = code[2:]
    for i in js:
        i['code'] = code
        with open('./data/NewFinanceAnalysis/zcfzb.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            info = i.values()
            writer.writerow(info)
    return



def get_zcfzb(code='sz300365'):
    base_url = 'http://emweb.securities.eastmoney.com/NewFinanceAnalysis/zcfzbAjax'
    response = request.get(base_url, params={'companyType':4, 'reportDateType':0, 'reportType':1 ,'code': code})
    if response.status_code != 200:
        response = get_shareholders(code)
    return response.json()



if __name__ == '__main__':
    CSVfile = open('./data/code_list.csv', 'r')
    readCSV = csv.reader(CSVfile, delimiter=',')

    js = get_zcfzb()
    write_zcfzb(js)

    for row in readCSV:
        code = row[1]
        js = get_zcfzb(code)
        save_MainTarget(js, code)

    CSVfile.close()
