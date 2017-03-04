from openpyxl import Workbook

lexicalEntries = 'lexicalEntries'

entries = 'entries'

senses = 'senses'

definitions = 'definitions'

examples = 'examples'

etymologies = 'etymologies'

class excelCreator:

    wb = Workbook()

    ws = wb.active

    @staticmethod
    def getEntrieOf(entrie):

        worddefinesStr = ''

        examplesStr = ''

        ety = ''

        if etymologies in entrie:

            for etymologie in entrie[etymologies]:
                ety += etymologie

        for sense in entrie[senses]:

            if definitions in sense:

                for define in sense[definitions]:
                    worddefinesStr += define + '\n'

            if examples in sense:

                for example in sense[examples]:
                    examplesStr += example['text'] + '\n'

        last = worddefinesStr.rfind('\n')

        if last != -1:
            worddefinesStr = worddefinesStr[:last]

        last = examplesStr.rfind('\n')

        if last != -1:
            examplesStr = examplesStr[:last]

        return worddefinesStr, examplesStr, ety

    @classmethod
    def getDefinetions(cls, item):

        if lexicalEntries not in item:
            return ''

        if entries not in item[lexicalEntries][0]:
            return ''

        val1 = ''

        val2 = ''

        val3 = ''

        for entrie in item[lexicalEntries][0][entries]:

            temptup = cls.getEntrieOf(entrie)

            val1 += temptup[0]

            val2 += temptup[1]

            val3 += temptup[2]

        return val1, val2, val3

    @classmethod
    def writeToExcel(cls, words, fileName):

        nIndex = 0

        for word in words:

            nIndex += + 1

            cls.ws['A' + str(nIndex)] = word['id']

            cls.ws['B' + str(nIndex)], cls.ws['C' + str(nIndex)], cls.ws['D' + str(nIndex)] = cls.getDefinetions(word)

        cls.wb.save(fileName)

__intance = 0

def instance():

    global  __intance

    if __intance == 0:

        __intance = excelCreator()

    return __intance





