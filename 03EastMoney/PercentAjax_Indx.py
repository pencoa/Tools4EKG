from WebRequest import WebRequest
from time import sleep
import requests
import csv
import json

request = WebRequest()


def save_PercentAjax_Indx(js, code='sz300365'):
    if not js:
        return
    code = code[2:]
    for i in js:
        i['code'] = code
        with open('./data/NewFinanceAnalysis/PercentAjax_Indx.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            info = i.values()
            writer.writerow(info)
    return



def get_PercentAjax_Indx(code='sz300365'):
    base_url = 'http://emweb.securities.eastmoney.com/NewFinanceAnalysis/PercentAjax_Indx'
    response = request.get(base_url, params={'code': code})
    if response.status_code != 200:
        response = get_shareholders(code)
    return response.json()



if __name__ == '__main__':
    CSVfile = open('./data/code_list.csv', 'r')
    readCSV = csv.reader(CSVfile, delimiter=',')

    for row in readCSV:
        code = row[1]
        js = get_PercentAjax_Indx(code)
        save_PercentAjax_Indx(js, code)

    CSVfile.close()
