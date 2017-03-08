import zerorpc
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

class wordFinding(object):

    def querylearned(self):

        words = getNeedReview()

        results = []

        for word in words:

            item = totalwords.instance().getWord(word)

            if item != 0:

                results.append(item)

        return str({'total':results})

    def queryword(self, word):

        item = totalwords.instance().getWord(word)

        return item

s = zerorpc.Server(wordFinding())

s.bind("tcp://127.0.0.1:4242")

s.run()