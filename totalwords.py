from pymongo import MongoClient

class totalWords:

    results = []

    def __init__(self):

        client = MongoClient('localhost', 27017)

        db = client["test"]

        origCollection = db['totalwords']

        client.close()

        self.results = origCollection.find({})

    def getWord(self, word):

        count = self.results.count()

        for i in range(count):

            item = self.results[i]

            if item['id'] == word:

                return item

        return 0

    def saveWithIndex(self):

        count = self.results.count()

        tempItems = []

        for i in range(count):

            item = self.results[i]

            item['index'] = i

            tempItems.append(item)

        client = MongoClient('localhost', 27017)

        db = client["test"]

        origCollection = db['temp']

        origCollection.insert_many(tempItems)

        client.close()

__intance = 0

def instance():

    global  __intance

    if __intance == 0:

        __intance = totalWords()

    return __intance