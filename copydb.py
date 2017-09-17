from pymongo import MongoClient

def getTotalWords():

    client = MongoClient('localhost', 27017)

    db = client["test"]

    coll = db['totalwords']

    totalwords = coll.find({})
    
    return totalwords

def cloneInNewDB():

    totalwords = getTotalWords()

    client = MongoClient('118.89.188.169', 27017)

    db = client["findwordmean"]

    coll = db['totalwords']
    
    coll.insert_many(totalwords)
    
    
cloneInNewDB()

