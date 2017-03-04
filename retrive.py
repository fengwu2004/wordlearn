# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import json
import pymongo

from pymongo import MongoClient

class totalWords:

    results = []

    @classmethod
    def instance(cls):

        return cls()

    def __init__(self):

        client = MongoClient('localhost', 27017)

        db = client["test"]

        origCollection = db['wordsnew_copy']

        self.results = origCollection.find({})

        print("init")