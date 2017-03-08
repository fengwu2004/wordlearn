import query_save
import totalwords
import createExcel
from pymongo import MongoClient

def getLines():

    lines = [line.rstrip('\n') for line in open('today.txt')]

    return lines

def addToLearned(words):

    client = MongoClient('localhost', 27017)

    db = client["test"]

    coll = db['learnedwords']

    wordswithkey = []

    for word in words:

        key = dict()

        key['id'] = word

        temp = coll.count({'id':word})

        if temp == 0:

            wordswithkey.append(key)

    if len(wordswithkey) > 0:

        coll.insert_many(wordswithkey)

    client.close()

def getNeedReview():

    client = MongoClient('localhost', 27017)

    db = client["test"]

    coll = db['learnedwords']

    needReviewWords = coll.find({})

    client.close()

    results = []

    for result in needReviewWords:

        results.append(result['id'])

    return results

def run():

    todaywords = getLines()

    addToLearned(todaywords)

    needReviewWords = getNeedReview()

    query_save.run(todaywords)

    createExcel.instance().create(todaywords, '/Users/yan/code/today.xlsx')

    createExcel.instance().create(needReviewWords, '/Users/yan/code/reivew.xlsx')

run()