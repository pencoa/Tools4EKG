from WebRequest import WebRequest
from time import sleep
from lxml import html
import requests
import csv
import json
import re

request = WebRequest()


# def parse_manageCompany(code='80163340'):
#     url = 'http://fund.eastmoney.com/Company/f10/jbgk_' + str(code) + '.html'
#     response = request.get(url)
#     mainfo = {}
#     mainfo['code'] = str(code)
#     company = html.fromstring(response.content.decode('utf-8'))
#     mainfo['fullname'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[1]/td[2]/text()")[0]
#     mainfo['englishname'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[2]/td[2]/text()")[0]
#     mainfo['type'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[3]/td[2]/text()")[0]
#     mainfo['estab_data'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[4]/td[2]/text()")[0]
#     mainfo['reg_cap'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[4]/td[3]/text()")[0]
#     mainfo['legal_person'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[5]/td[2]/text()")[0]
#     mainfo['president_manager'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[5]/td[4]/text()")[0]
#     mainfo['reg_address'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[6]/td[2]/text()")[0]
#     mainfo['address'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[7]/td[2]/text()")[0]
#     mainfo['website'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[8]/td[2]/text()")[0]
#     mainfo['postcode'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[9]/td[2]/text()")[0]
#     mainfo['ser_mail'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[9]/td[4]/text()")[0]
#     mainfo['telephone'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[10]/td[2]/text()")[0]
#     mainfo['fax'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[10]/td[4]/text()")[0]
#     mainfo['business_scope'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[11]/td[2]/text()")[0]
#     mainfo['fund_num'] = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[11]/td[2]/text()")[0]
#     manage_size = company.xpath("/html/body/div[1]/div[1]/div[5]/div[3]/div[2]/table/tr[13]/td[2]/text()")[0]
#     mainfo['manage_size'] = re.sub('\s', '', manage_size)
#     with open('./data/Fund/fundCompany.csv', 'a') as csv_file:
#         writer = csv.writer(csv_file, delimiter=',')
#         writer.writerow(mainfo.values())
#     return
#
#
# def parse_bank(bank_code='80001068'):
#     bank_code = str(bank_code)
#     url = 'http://fund.eastmoney.com/bank/' + bank_code + '.html'
#     response = request.get(url)
#     bank = html.fromstring(response.content.decode('gbk'))
#     bkinfo = {}
#     bkinfo['code'] = bank_code
#     bkinfo['fullname'] = bank.xpath("//*[@id='tableMainDiv']/table/tr[2]/td[2]/a")[0].text
#     bkinfo['englishname'] = bank.xpath("//*[@id='tableMainDiv']/table/tr[2]/td[4]/text()")[0]
#     bkinfo['estab_data'] = bank.xpath("//*[@id='tableMainDiv']/table/tr[3]/td[2]/text()")[0]
#     bkinfo['reg_cap'] = bank.xpath("//*[@id='tableMainDiv']/table/tr[3]/td[4]/text()")[0]
#     bkinfo['legal_person'] = bank.xpath("//*[@id='tableMainDiv']/table/tr[4]/td[2]/text()")[0]
#     bkinfo['president_manager'] = bank.xpath("//*[@id='tableMainDiv']/table/tr[4]/td[4]/text()")[0]
#     bkinfo['address'] = bank.xpath("//*[@id='tableMainDiv']/table/tr[5]/td[2]/text()")[0]
#     bkinfo['website'] = bank.xpath("//*[@id='tableMainDiv']/table/tr[5]/td[4]/text()")[0]
#     bkinfo['postcode'] = bank.xpath("//*[@id='tableMainDiv']/table/tr[6]/td[2]/text()")[0]
#     bkinfo['ser_mail'] = bank.xpath("//*[@id='tableMainDiv']/table/tr[6]/td[4]/text()")[0]
#     bkinfo['telephone'] = bank.xpath("//*[@id='tableMainDiv']/table/tr[7]/td[2]/text()")[0]
#     bkinfo['fax'] = bank.xpath("//*[@id='tableMainDiv']/table/tr[7]/td[4]/text()")[0]
#     bkinfo['business_scope'] = bank.xpath("//*[@id='tableMainDiv']/table/tr[8]/td[2]/text()")[0]
#     with open('./data/Fund/bank.csv', 'a') as csv_file:
#         writer = csv.writer(csv_file, delimiter=',')
#         writer.writerow(bkinfo.values())
#     return
#
#
# def parse_fundmanager(macode='30139111'):
#     macode = str(macode)
#     url = 'http://fund.eastmoney.com/manager/' + macode + '.html'
#     response = request.get(url)
#     fundma = html.fromstring(response.content.decode('utf-8'))
#     mainfo = {}
#     mainfo['macode'] = macode
#     name = fundma.xpath("//*[@id='name_1']/text()")
#     if name is not None:
#         mainfo['name'] = name
#     else:
#         mainfo['name'] = ' '
#     start_data = fundma.xpath("/html/body/div[6]/div[2]/div[1]/div/div[2]/div[2]/text()")[3]
#     start_data = re.sub('\s','',start_data)
#     mainfo['start_data'] = start_data
#     intro = fundma.xpath("/html/body/div[6]/div[2]/div[1]/div/div[1]/p")[0].text_content()
#     mainfo['intro'] = re.sub('\s','',intro)
#     cmurl = fundma.xpath("/html/body/div[6]/div[2]/div[1]/div/div[2]/div[2]/a")[0].attrib['href']
#     cmcode = re.search('[\d]+', cmurl).group(0)
#     mainfo['workin'] = cmcode
#     with open('./data/Fund/fundma.csv', 'a') as csv_file:
#         writer = csv.writer(csv_file, delimiter=',')
#         writer.writerow(mainfo.values())
#     fundlist = fundma.xpath("/html/body/div[6]/div[2]/div[1]/table/tbody/tr")
#
#     for tr in fundlist:
#         ma2fund = {}
#         ma2fund['macode'] = macode
#         tbs = tr.xpath("./td")
#         fcode = tbs[0]
#         ma2fund['fcode'] = fcode.xpath("./a")[0].text
#         fundname = tbs[1]
#         ma2fund['fundname'] = fundname.xpath("./a")[0].text
#         ma2fund['period'] = tbs[5].text
#         with open('./data/Fund/ma2fund.csv', 'a') as CSV_file:
#             writer = csv.writer(CSV_file, delimiter=',')
#             writer.writerow(ma2fund.values())
#     return



def parse_fund(code):
    base_url = 'http://fund.eastmoney.com/f10/'
    url = base_url + str(code) + '.html'
    response = request.get(url)
    info = {}
    info['code'] = str(code)
    fund = html.fromstring(response.content.decode('utf-8'))
    info['fullname'] = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[1]/td[1]/text()")[0]
    info['shortname'] = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[1]/td[2]/text()")[0]
    info['type'] = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[2]/td[2]/text()")[0]
    issue_data = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[3]/td[1]")[0]
    if issue_data.text is not None:
        info['issue_data'] = re.sub('日','',re.sub('[年|月]','-',issue_data.text))
    else:
        info['issue_data'] = ' '
    estab = fund.xpath("//*[@id='bodydiv']/div[8]/div[3]/div[2]/div[3]/div/div[1]/table/tr[3]/td[2]/text()")[0]
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
