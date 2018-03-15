from WebRequest import WebRequest
from time import sleep
from lxml import html
import requests
import csv
import json
import re

request = WebRequest()

def check_get(fund, xpath):
    data = fund.xpath(xpath)[0]
    if data.text is not None:
        return data.text
    else:
        return ' '



def parse_fund(code):
    code = str(code)
    base_url = 'http://fund.eastmoney.com/f10/'
    url = base_url + code + '.html'
    response = request.get(url)
    info = {}
    info['code'] = code
    fund = html.fromstring(response.content.decode('utf-8'))
    info['fullname'] = check_get(fund, "//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[1]/td[1]")
    info['shortname'] = check_get(fund, "//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[1]/td[2]")
    info['type'] = check_get(fund, "//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[2]/td[2]")
    info['issue_data'] = check_get(fund, "//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[3]/td[1]")
    estab = check_get(fund, "//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[3]/td[2]")
    estab_data = re.search('.*日',estab).group(0)
    info['estab_data'] = re.sub('日','',re.sub('[年|月]','-',estab_data))
    info['estab_size'] = re.search(' ([0-9.]+.*份)',estab).group(0)

    
    info['scale'] = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[4]/td[1]/text()")[0]
    info['size'] = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[4]/td[2]/a/text()")[0] + \
                    fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[4]/td[2]/text()")[0]
    manage_url = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[5]/td[1]/a")[0].attrib['href']
    manage_code = re.search('[\d]+', manage_url)
    if manage_code is not None:
        info['manage_code'] = manage_code.group[0]
    else:
        info['manage_code'] = ' '
    # parse_manageCompany(manage_code)

    bank_url = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[5]/td[2]/a")[0].attrib['href']
    bank_code = re.search('[\d]+', bank_url).group(0)
    if bank_code is not None:
        info['bank_code'] = bank_code.group[0]
    else:
        info['bank_code'] = ' '

    # parse_bank(bank_code)
    # managers = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[6]/td[1]/a")
    # for manager in managers:
    #     maurl = manager.attrib['href']
    #     macode = re.search('[\d]+', maurl).group(0)
        # parse_fundmanager(macode)
    info['mafee'] = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[7]/td[1]/text()")[0]
    info['trustfee'] = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[7]/td[2]/text()")[0]
    info['salefee'] = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[8]/td[1]/text()")[0]
    info['subsfee'] = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[8]/td[2]/text()")[0]
    info['subsfee1'] = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[9]/td[1]/text()")[0]
    info['subsfee2'] = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[9]/td[2]/text()")[0]

    # baseline = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[10]/td[1]")
    # if baseline is not None:
    #     info['baseline'] = baseline[0].text
    # else:
    #     info['baseline'] = ' '
    #
    # trace = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[10]/td[2]")
    # if trace is not None:
    #     info['trace'] = trace[0].text
    # else:
    #     info['trace'] = ' '

    aims = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[2]/div/p")[0]
    if aims.text is not None:
        info['aims'] = re.sub('\s','',aims.text)
    else:
        info['aims'] = ' '

    mind = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[3]/div/p")[0]
    if mind.text is not None:
        info['mind'] = re.sub('\s','',mind.text)
    else:
        info['mind'] = ' '

    business_scope = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[4]/div/p")[0]
    if business_scope.text is not None:
        info['business_scope'] = re.sub('\s','',business_scope.text)
    else:
        info['business_scope'] = ' '

    strategy = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[5]/div/p")[0]
    if strategy.text is not None:
        info['strategy'] = re.sub('\s','',strategy.text)
    else:
        info['strategy'] = ' '

    strategy1 = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[6]/div/p")[0]
    if strategy1.text is not None:
        info['strategy1'] = re.sub('\s','',strategy1.text)
    else:
        info['strategy1'] = ' '

    risk = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[8]/div/p")[0]
    if risk.text is not None:
        info['risk'] = re.sub('\s','',risk.text)
    else:
        info['risk'] = ' '

    with open('./data/Fund/fund.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(info.values())
    return



if __name__ == '__main__':
    CSVfile = open('./data/fundcode_list.csv', 'r')
    readCSV = csv.reader(CSVfile, delimiter=',')

    for row in readCSV:
        code = row[0]
        parse_fund(code)

    CSVfile.close()
