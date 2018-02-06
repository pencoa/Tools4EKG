import csv
import re


with open('./data/share_person.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    titles = ['shareholder','value','percent','share_type','share_code']
    writer.writerow(titles)


with open('./data/share_fund.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    titles = ['shareholder','value','percent','share_type','share_code']
    writer.writerow(titles)


with open('./data/share_company.csv', 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    titles = ['shareholder','value','percent','share_type','share_code']
    writer.writerow(titles)



with open('./data/shareholder.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    for row in readCSV:
        if len(row[0]) > 4:
            if '基金' in row[0] or 'FUND' in row[0]:
                with open('./data/share_fund.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    writer.writerow(row)
                continue
            else:
            # elif '公司' in row[0] or 'LIMITED' in row[0] or '有限合伙' in row[0] or 'BANK' in row[0] or 'UBSAG' in row[0]:
                with open('./data/share_company.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile, delimiter=',')
                    writer.writerow(row)
                continue
        if len(row[0]) <= 4:
            with open('./data/share_person.csv', 'a') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(row)
            continue
