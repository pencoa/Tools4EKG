from WebRequest import WebRequest
from time import sleep
import requests
import csv
import json

request = WebRequest()

def write_xjllb(js, code='sz300365'):
    if not js:
        return
    with open('./data/NewFinanceAnalysis/xjllb.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        info = js[0].keys()
        writer.writerow(info)
    return

def save_xjllb(js, code='sz300365'):
    if not js:
        return
    code = code[2:]
    for i in js:
        i['code'] = code
        with open('./data/NewFinanceAnalysis/xjllb.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            info = i.values()
            writer.writerow(info)
    return



def get_xjllb(code='sz300365'):
    base_url = 'http://emweb.securities.eastmoney.com/NewFinanceAnalysis/xjllbAjax'
    response = request.get(base_url, params={'companyType':4, 'reportDateType':0, 'reportType':1 ,'code': code})
    if response.status_code != 200:
        response = get_shareholders(code)
    jl = response.json()
    js = json.loads(jl)
    return js


if __name__ == '__main__':
    CSVfile = open('./data/code_list.csv', 'r')
    readCSV = csv.reader(CSVfile, delimiter=',')

    js = get_xjllb()
    write_xjllb(js)

    for row in readCSV:
        code = row[1]
        js = get_xjllb(code)
        save_xjllb(js, code)

    CSVfile.close()
