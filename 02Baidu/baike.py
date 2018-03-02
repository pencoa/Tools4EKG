from WebRequest import WebRequest

request = WebRequest()

listed = open('./listed_company.csv', 'r')
for line in listed:
    cmname = line.strip()
    try:
        response = request.get('https://baike.baidu.com/item/' + cmname)
        # create baikepage directory before this step
        with open('./baikepage/%s.html' % cmname, 'w+') as f:
            f.write(response.content.decode('utf8'))
    except Exception as e:
        print('It failed :(', e.__class__.__name__)
listed.close()
