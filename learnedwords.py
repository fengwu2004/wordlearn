from pymongo import MongoClient
import totalwords
import createExcel

class learnedMgr:

    def addTo(self, words):

        client = MongoClient('localhost', 27017)

        db = client["test"]

        origCollection = db['learnedwords']

        origCollection.insert_many(words)

        client.close()

    def createNeedReview(self):

        client = MongoClient('localhost', 27017)

        db = client["test"]

        origCollection = db['learnedwords']

        results = origCollection.find({})

        items = []

        for unit in results:

            temp = totalwords.instance().getWord(unit)

            if temp != 0:

                items.append(temp)

        client.close()

        createExcel.instance().writeToExcel(items, '/Users/yan/code/review.xlsx')

__intance = 0

def instance():

    global  __intance

    if __intance == 0:

        __intance = learnedMgr()

    return __intance