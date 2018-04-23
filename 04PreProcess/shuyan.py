from WebRequest import WebRequest
from time import sleep

request = WebRequest()

ment2ent = "http://shuyantech.com/api/cndbpedia/ment2ent"
params = {'apikey' : '6c6032bdc2d2b043133f2a176f677bb'}


ent_list = []
f = open('./data/people.csv', 'r')
for line in f:
    line = line.strip()
    params['q'] = line
    response = request.get(ment2ent, params)
    sleep(0.7)
    # if 'ret' not in response.json().keys(): continue
    ents = response.json()['ret']
    if len(ents) == 0: continue
    for i in ents:
        with open('./data/people_entity.txt', 'a') as file:
            file.write("%s\n" % i)

f.close()
