

import createExcel
import totalwords

def getLines():

    lines = [line.rstrip('\n') for line in open('today.txt')]

    return lines

class todaylearner:

    @classmethod
    def createExcal(cls):

        lines = getLines()

        words = []

        for line in lines:

            result = totalwords.instance().getWord(line)

            if result != 0:

                words.append(result)

        createExcel.instance().writeToExcel(words, "/Users/yan/code/today.xlsx")

todaylearner.createExcal()