import numpy
import totalwords
import wordParser
from pymongo import MongoClient

class wordNet:

    def __init__(self):

        self.count = totalwords.instance().results.count()

        self.matrix = numpy.zeros((self.count, self.count), dtype=numpy.int)

        self.words = totalwords.instance().results

    @staticmethod
    def checkHanveConnection(first, second):

        return 1

        if first['id'] in second['def']:

            return 1

        if first['id'] in second['exam']:

            return 1

        if first['id'] in second['ety']:

            return 1

        if second['id'] in first['def']:

            return 1

        if second['id'] in first['exam']:

            return 1

        if second['id'] in first['ety']:

            return 1

        return 0

    def createNet(self):

        for i in range(self.count):

            self.matrix[i][i] = 1

        for i in range(self.count):

            for j in range(self.count):

                if j <= i:

                    self.matrix[i][j] = self.matrix[j][i]

                else:

                    b = self.checkHanveConnection(self.words[i], self.words[j])

                    self.matrix[i][j] = b

            m = self.matrix[i].tostring()

            item = self.words[i]

            item['links'] = m

            print(i)

        self.save()

        print('结束了')

    def save(self):

        client = MongoClient('localhost', 27017)

        db = client["test"]

        origCollection = db['withLinks']

        origCollection.insert_many(self.words)

        client.close()

__intance = 0

def instance():

    global  __intance

    if __intance == 0:

        __intance = wordNet()

    return __intance

instance().createNet()