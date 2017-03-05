

import createExcel
import totalwords
import time

def getLines():

    lines = [line.rstrip('\n') for line in open('today.txt')]

    return lines

class todaylearner:

    @classmethod
    def createExcal(cls):

        lines = getLines()

        words = []

        lasttime = time.time()

        for line in lines:

            result = totalwords.instance().getWord(line)

            if result != 0:

                words.append(result)

        lasttime = time.time() - lasttime

        print('时间花费', lasttime)

        createExcel.instance().writeToExcel(words, "/Users/yan/code/today.xlsx")

todaylearner.createExcal()