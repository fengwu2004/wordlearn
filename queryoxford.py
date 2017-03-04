# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests

lines = [line.rstrip('\n') for line in open('tsst.txt')]

app_id = 'ae2cbddb'

app_key = '3270633624384b8820750597771dbe95'

language = 'en'

results = []

nIndex = 0

nTotalCount = len(lines)

def queryOxford(word):

    global nIndex

    word_id = word

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key, "Accept":"application/json"})

    try:
        temp = r.json()
    except:
        print("异常")
    else:
        results.append(temp)

    if nIndex < nTotalCount and nIndex + 1 < nTotalCount:

        print("请求中",  nIndex)

        nIndex += 1

        word = lines[nIndex]

        queryOxford(word)

    else:

        print("q请求结束")

queryOxford(lines[0])

def saveToMongoDB():

    from pymongo import MongoClient

    client = MongoClient('localhost', 27017)

    db = client["test"]

    collection = db['words']

    collection.insert_many(results)

saveToMongoDB()