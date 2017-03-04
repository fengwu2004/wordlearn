from pymongo import MongoClient

class totalWords:

    results = []

    def __init__(self):

        client = MongoClient('localhost', 27017)

        db = client["test"]

        origCollection = db['totalwords']

        self.results = origCollection.find({})

    def getWord(self, word):

        count = self.results.count()

        for i in range(count):

            item = self.results[i]

            if item['id'] == word:

                return item

        return 0

__intance = 0

def instance():

    global  __intance

    if __intance == 0:

        __intance = totalWords()

    return __intance