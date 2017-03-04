import numpy
import totalwords
import wordParser

class wordNet:

    def __init__(self):

        self.count = totalwords.instance().results.count()

        self.matrix = numpy.zeros((self.count, self.count))

        self.words = totalwords.instance().results

    @staticmethod
    def checkHanveConnection(first, second):

        tub = wordParser.getEntrieOf(second)

        if first['id'] in tub[0]:

            return 1

        if first['id'] in tub[1]:

            return 1

        if first['id'] in tub[2]:

            return 1

        tub = wordParser.getEntrieOf(first)

        if second['id'] in tub[0]:

            return 1

        if second['id'] in tub[1]:

            return 1

        if second['id'] in tub[2]:

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

                    print(b)

                    self.matrix[i][j] = b


__intance = 0

def instance():

    global  __intance

    if __intance == 0:

        __intance = wordNet()

    return __intance