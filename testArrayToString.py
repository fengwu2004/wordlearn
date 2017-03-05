import numpy

matrix = numpy.zeros((100, 100), dtype=numpy.int)

matrix[0][99] = 1


from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client["test"]

def insert():

    origCollection = db['abcd']

    results = origCollection.find({})

    r = results[0]

    print(r, results[0])

    r['index'] = matrix[0].tostring()

    coll = db['accd_1']

    coll.insert_one(r)

def read():

    coll = db['accd_1']

    results = coll.find({})

    v = results[0]['index']

    f = numpy.fromstring(v, dtype=int)

    for c in range(len(f)):
        print(f[c])

    client.close()

insert()