import totalwords
from pymongo import MongoClient

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

def getTotalWord():
    
    client = MongoClient('localhost', 27017)
    
    db = client["test"]
    
    coll = db['totalwords']
    
    needReviewWords = coll.find({})
    
    client.close()
    
    results = []
    
    for result in needReviewWords:
        
        results.append(result['id'])
    
    return results


def getNextLearn():
    
    already = getNeedReview()
    
    total = getTotalWord()
    
    result = []
    
    for word in total:
        
        if word not in already:
            
            result.append(word)
        
        if len(result) > 600:
            
            break

    for item in result:
        
        print(item)

getNextLearn()
