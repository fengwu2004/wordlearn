from pymongo import MongoClient
import wordParser
import time

class totalWords:

    results = []

    def __init__(self):

        client = MongoClient('localhost', 27017)

        db = client["test"]

        origCollection = db['origin(not delete)']

        client.close()

        self.results = origCollection.find({})

    def getWord(self, word):

        count = self.results.count()

        for i in range(count):

            item = self.results[i]

            itemId = item['id']

            itemId = itemId.replace('_', ' ')

            if itemId == word:

                return item

        return 0

    def saveWithIndex(self):

        count = self.results.count()

        tempItems = []

        for i in range(count):

            item = self.results[i]['results'][0]

            item['index'] = i

            tup = wordParser.getEntrieOf(item)

            item['def'] = tup[0]

            item['exam'] = tup[1]

            item['ety'] = tup[2]

            tempItems.append(item)

        client = MongoClient('localhost', 27017)

        db = client["test"]

        origCollection = db['totalwords']

        origCollection.insert_many(tempItems)

        client.close()

__intance = 0

def instance():

    global  __intance

    if __intance == 0:

        __intance = totalWords()

    return __intance

instance().saveWithIndex()