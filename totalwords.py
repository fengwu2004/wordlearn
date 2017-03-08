from pymongo import MongoClient
import wordParser
import time

class totalWords:

    results = []

    def __init__(self):

        client = MongoClient('localhost', 27017)

        db = client["test"]

        self.origCollection = db['totalwords']

        self.results = self.origCollection.find({})

    def checkExist(self, word):

        return self.origCollection.count({'id': word}) != 0

    def getWord(self, word):

        if self.origCollection.count({'id':word}) == 0:

            return 0

        result = self.origCollection.find({'id':word})

        return result[0]

    def saveWithIndex(self):

        count = self.results.count()

        tempItems = []

        for i in range(count):

            item = self.results[i]

            item['index'] = i

            item['def'] = item['def']

            item['exam'] = item['exam']

            item['ety'] = item['ety']

            tempItems.append(item)

        client = MongoClient('localhost', 27017)

        db = client["test"]

        origCollection = db['temp']

        origCollection.insert_many(tempItems)

        client.close()

    def save(self, words):

        client = MongoClient('localhost', 27017)

        db = client["test"]

        origCollection = db['totalwords']

        origCollection.insert_many(words)

        client.close()

__intance = 0

def instance():

    global  __intance

    if __intance == 0:

        __intance = totalWords()

    return __intance