import csv


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
        print(row[0])
