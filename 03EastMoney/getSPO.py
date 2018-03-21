from pymongo import MongoClient

def finder(entity):
    client = MongoClient()
    db = client['QAdb']
    ans_rt = []
    for u in db.posts.find({'head':entity}):
        ans_rt.append((u['relation'],u['tail']))
    return (entity,ans_rt)


if __name__ == '__main__':
    with open('./data/CompanySurvey/lawoffice.txt', 'r') as file:
        for line in file:
            spo = finder(line)
            for u in spo:
                print(u)
