from WebRequest import WebRequest
from time import sleep
import requests
import csv
import json

request = WebRequest()


def save_gdrs(js, code='sz300365'):
    code = code[2:]
    for i in js['gdrs']:
        with open('./data/ShareHoldersResearch/gdrs.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            i['code'] = code
            info = i.values()
            writer.writerow(info)
    return


def save_sdltgd(js, code='sz300365'):
    code = code[2:]
    for i in js['sdltgd']:
        lt = i['sdltgd']
        for j in lt:
            with open('./data/ShareHoldersResearch/sdltgd.csv', 'a') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                j['code'] = code
                info = j.values()
                writer.writerow(info)
    return


def save_sdgd(js, code='sz300365'):
    code = code[2:]
    for i in js['sdgd']:
        lt = i['sdgd']
        for j in lt:
            with open('./data/ShareHoldersResearch/sdgd.csv', 'a') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                j['code'] = code
                info = j.values()
                writer.writerow(info)
    return


def save_jjcg(js, code='sz300365'):
    code = code[2:]
    if not js['jjcg']:
        return
    for i in js['jjcg']:
        rq = i['rq']
        cg = i['jjcg']
        for j in cg:
            with open('./data/ShareHoldersResearch/jjcg.csv', 'a') as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                j['code'] = code
                j['rq']   = rq
                info = j.values()
                writer.writerow(info)
    return


def save_xsjj(js, code='sz300365'):
    code = code[2:]
    if not js['xsjj']:
        return
    for i in js['xsjj']:
        with open('./data/ShareHoldersResearch/xsjj.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            i['code'] = code
            info = i.values()
            writer.writerow(info)
    return


def get_shareholders(code='sz300365'):
    base_url = 'http://emweb.securities.eastmoney.com/PC_HSF10/ShareholderResearch/ShareholderResearchAjax'
    response = request.get(base_url, params={'code': code})
    if response.status_code != 200:
        response = get_shareholders(code)
    return response.json()


def test():
    try:
        js = get_shareholders()
    except (ValueError, OSError) as e:
        print(e)
    save_gdrs(js)
    save_sdltgd(js)
    save_sdgd(js)
    save_jjcg(js)
    save_xsjj(js)
    return


if __name__ == '__main__':
    CSVfile = open('./data/code_list.csv', 'r')
    readCSV = csv.reader(CSVfile, delimiter=',')

    for row in readCSV:
        code = row[1]
        try:
            # sleep(2)
            js = get_shareholders(code)
            # sleep(2)
            save_gdrs(js, code)
            save_sdltgd(js, code)
            save_sdgd(js, code)
            save_jjcg(js, code)
            save_xsjj(js, code)
        except (ValueError, OSError, ConnectionError) as e:
            print(e)
        # sleep(2)
        # save_gdrs(js, code)
        # save_sdltgd(js, code)
        # save_sdgd(js, code)
        # save_jjcg(js, code)
        # save_xsjj(js, code)

    CSVfile.close()
