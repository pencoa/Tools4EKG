import requests
from time import sleep


url_get_base = "http://api.ltp-cloud.com/analysis/"
params = {
    'api_key' : 'Q1N7A821B8QbwCmcjDcvRtBudTMwyttwNZcI4M5v',
    'text' : '陈玮1984年毕业于华东师范大学心理学系，获得学士学位。\n',
    'pattern' : 'pos',
    'format' : 'plain'
}


f = open('./data/experiences.csv', 'r')
for line in f:
    line = line.strip()
    if len(line) > 100:
        line_list = line.split('。')
        for i in line_list:
            params['text'] = i
            response = requests.get(url_get_base, params=params)
            with open('./data/ltp_experience.csv', 'a') as file:
                file.write(response.content.decode('utf-8'))
                file.write('。\n')
    else:
        params['text'] = line
        response = requests.get(url_get_base, params=params)
        with open('./data/ltp_experience.csv', 'a') as file:
            file.write(response.content.decode('utf-8'))
            file.write('\n\n')
    sleep(0.5)

f.close()
