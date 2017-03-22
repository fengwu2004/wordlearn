import totalwords
from pymongo import MongoClient
import urllib.request


def getLines():

    lines = [line.rstrip('\n') for line in open('today.txt')]

    return lines

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
    
    totals = coll.find({})
    
    client.close()
    
    results = []
    
    for result in totals:
        
        results.append(result)
    
    return results

def run():
    
    reviews = getLines()
    
    totals = getTotalWord()
    
    results = []
    
    for word in totals:
        
        if word['id'] in reviews:
            
            if 'lexicalEntries' in word:
                
                if 'pronunciations' in word['lexicalEntries'][0]:
                    
                    if 'audioFile' in word['lexicalEntries'][0]['pronunciations'][0]:
                        
                        results.append({'id':word['id'], 'url':word['lexicalEntries'][0]['pronunciations'][0]['audioFile']})
    
    for item in results:
        
        print(item['url'])
        
        request = urllib.request.urlopen(item['url'], timeout = 10)

        with open('/Users/yan/Desktop/mp3_2/' + item['id'] + '.mp3', 'wb') as f:
            
            try:
                f.write(request.read())
                
            except:
                print("error")


run()

print('完毕')