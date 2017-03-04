from pymongo import MongoClient

class learnedMgr:

    alreadylearned = []

    def __init__(self):

        client = MongoClient('localhost', 27017)

        db = client["test"]

        origCollection = db['learnedwords']

        self.results = origCollection.find({})

        print("init")

__intance = 0

def instance():

    global  __intance

    if __intance == 0:

        __intance = learnedMgr()

    return __intance