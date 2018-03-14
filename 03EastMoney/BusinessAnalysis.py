from WebRequest import WebRequest
from time import sleep
import requests
import csv
import json

request = WebRequest()


def save_zyfw(js, code='sz300365'):
    code = code[2:]
    if js['zyfw'] is None:
        return
    if len(js['zyfw']) == 0:
        return
    ms = js['zyfw'][0]['ms']
    with open('./data/BusinessAnalysis/zyfw.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        info = [code, ms]
        writer.writerow(info)
    return


def save_jyps(js, code='sz300365'):
    code = code[2:]
    if js['jyps'] is None:
        return
    if len(js['jyps']) == 0:
        return
    ms = js['jyps'][0]['ms']
    with open('./data/BusinessAnalysis/jyps.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        info = [code, ms]
        writer.writerow(info)
    return


def save_hy(js, code='sz300365'):
    code = code[2:]
    if js['zygcfx'] is None:
        return
    if len(js['zygcfx']) == 0:
        return
    if js['zygcfx'][0]['hy'] is None:
        return
    for i in js['zygcfx']:
        hyj = i['hy']
        for j in hyj:
            j['code'] = code
            with open('./data/BusinessAnalysis/hy.csv', 'a') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                info = j.values()
                writer.writerow(info)
    return


def save_cp(js, code='sz300365'):
    code = code[2:]
    if js['zygcfx'] is None:
        return
    if len(js['zygcfx']) == 0:
        return
    if js['zygcfx'][0]['cp'] is None:
        return
    for i in js['zygcfx']:
        cpj = i['cp']
        for j in cpj:
            j['code'] = code
            with open('./data/BusinessAnalysis/cp.csv', 'a') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                info = j.values()
                writer.writerow(info)
    return


def save_qy(js, code='sz300365'):
    code = code[2:]
    if js['zygcfx'] is None:
        return
    if len(js['zygcfx']) == 0:
        return
    if js['zygcfx'][0]['qy'] is None:
        return
    for i in js['zygcfx']:
        qyj = i['qy']
        for j in qyj:
            j['code'] = code
            with open('./data/BusinessAnalysis/qy.csv', 'a') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                info = j.values()
                writer.writerow(info)
    return


def get_businessanalysis(code='sz000001'):
    base_url = 'http://emweb.securities.eastmoney.com/PC_HSF10/BusinessAnalysis/BusinessAnalysisAjax'
    response = request.get(base_url, params={'code': code})
    if response.status_code != 200:
        response = get_shareholders(code)
    return response.json()



if __name__ == '__main__':
    CSVfile = open('./data/code_list.csv', 'r')
    readCSV = csv.reader(CSVfile, delimiter=',')

    for row in readCSV:
        code = row[1]
        js = get_businessanalysis(code)
        save_zyfw(js, code)
        save_jyps(js, code)
        save_hy(js, code)
        save_cp(js, code)
        save_qy(js, code)

    CSVfile.close()
