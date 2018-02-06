# -*- coding: utf-8 -*-
"""
crawl cninfo website and store information as csv file.
the csv file is stored in data folder.
"""

from time import sleep
from lxml import html
import requests
import re
import csv

url = 'http://www.cninfo.com.cn/cninfo-new/information/companylist'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

response = requests.get(url, headers = headers)
tree = html.fromstring(response.content.decode('UTF-8'))
companylist = tree.xpath("//*/div[@class='list-ct']/div/ul/li/a[@target='_blank']")


with open('./brief.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    titles = ['share_code','company','english_name','address','shortname','legal_person','security','registrated_fund','Principal activities','post code','telephone','fax','website','listed time','prospectus time','Circulation','issue time','PE ration','issuing way','lead underwriter','listing sponsor','sponsor institution']
    writer.writerow(titles)


with open('./manager.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    titles = ['name','position','birth_year','gender','education_background','share_code']
    writer.writerow(titles)


with open('./shareholder.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    titles = ['shareholder','value','percent','share_type','share_code']
    writer.writerow(titles)


def brief_info(brief_link='http://www.cninfo.com.cn/information/brief/szmb000001.html', share_code='000001'):
    """
    parse and store companies' brief information
    """
    brief_response = requests.get(brief_link, headers = headers)
    brief = html.fromstring(brief_response.content.decode('gbk'))
    brief_info = list(map(lambda x : x.text.split('\r')[0], brief.xpath("//*/tr/td[@class='zx_data2']")))
    share = [share_code]
    info = share + brief_info
    with open('./brief.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(info)
    return


def manager_info(management_link='http://www.cninfo.com.cn/information/management/szmb000001.html', share_code='000001'):
    """
    parse and store companies' managers' information
    """
    manager_response = requests.get(management_link, headers=headers)
    manager = html.fromstring(manager_response.content.decode('gbk'))
    manager_list = manager.xpath("/html/body/div[2]/div[1]/div[2]/table/tr")
    for cmanager in manager_list[1:]:
        person_info = []
        for feature in cmanager.getchildren():
            person_info.append(re.sub(' ', '', re.sub('\r\n','',feature.text)))
        person_info.append(share_code)
        with open('./manager.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(person_info)
    return


def shareholders_info(shareholders_link='http://www.cninfo.com.cn/information/shareholders/000001.html', share_code='000001'):
    """
    parse and store shareholders's information
    """
    shareholders_response = requests.get(shareholders_link, headers=headers)
    share = html.fromstring(shareholders_response.content.decode('gbk'))
    shareholders_list = share.xpath("/html/body/div/div[1]/div/table/tr/td")[6:46]
    for i in range(int(len(shareholders_list)/4)):
        name    = shareholders_list[4*i].text
        name    = re.sub('[0-9]+\.', '', name)
        name    = re.sub(' ', '', name)
        fund    = shareholders_list[4*i+1].text
        fund    = re.sub(',', '', fund)
        fund    = re.sub(' ', '', fund)
        percent = shareholders_list[4*i+2].text
        percent = re.sub(' ', '', percent)
        stype   = shareholders_list[4*i+3].text
        stype   = re.sub(' ', '', stype)
        holder_info = [name, fund, percent, stype, share_code]
        with open('./shareholder.csv', 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(holder_info)
    return



for company in companylist:
    matchObj = re.search('(^[0-9]+) (.*)', company.text)
    share_code = matchObj.group(1)
    company_name = matchObj.group(2)
    company_link = company.get('href')
    matchSub = re.search('.*companyinfo_n\.html\?fulltext\?([a-z0-9]+)$' ,company_link)
    if matchSub is None: continue
    company_code = matchSub.group(1)
    brief_link        = 'http://www.cninfo.com.cn/information/brief/' + company_code + '.html'           # 公司概况
    management_link   = 'http://www.cninfo.com.cn/information/management/' + company_code + '.html'      # 高管人员
    shareholders_link = 'http://www.cninfo.com.cn/information/circulateshareholders/' + share_code + '.html'      # 十大股东
    brief_info(brief_link, share_code)
    sleep(5)
    manager_info(management_link, share_code)
    sleep(5)
    shareholders_info(shareholders_link, share_code)
    sleep(5)


# use this to reconnect when you meet ConnectError
# with open('./remain.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for row in readCSV:
#         company_code = row[2]
#         share_code = row[2][-6:]
#         brief_link        = 'http://www.cninfo.com.cn/information/brief/' + company_code + '.html'           # 公司概况
#         management_link   = 'http://www.cninfo.com.cn/information/management/' + company_code + '.html'      # 高管人员
#         shareholders_link = 'http://www.cninfo.com.cn/information/circulateshareholders/' + share_code + '.html'      # 十大股东
#         brief_info(brief_link, share_code)
#         manager_info(management_link, share_code)
#         shareholders_info(shareholders_link, share_code)
