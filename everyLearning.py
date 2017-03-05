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

    coll.insert_many(words)

    client.close()

def getNeedReview():

    client = MongoClient('localhost', 27017)

    db = client["test"]

    coll = db['learnedwords']

    result = coll.find({})

    client.close()

    return result

def run():

    todaywords = getLines()

    query_save.run(todaywords)

    addToLearned(todaywords)

    needReviewWords = getNeedReview()

    createExcel.instance().create(todaywords, '/Users/yan/code/today.xlsx')

    createExcel.instance().create(needReviewWords, '/Users/yan/code/reivew.xlsx')

run()