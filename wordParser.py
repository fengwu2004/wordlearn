lexicalEntries = 'lexicalEntries'

entries = 'entries'

senses = 'senses'

definitions = 'definitions'

examples = 'examples'

etymologies = 'etymologies'

def getEntrieOf(item):

    val1 = ''

    val2 = ''

    val3 = ''

    if lexicalEntries not in item:

        return val1, val2, val3

    for lex in item[lexicalEntries]:

        for entrie in lex[entries]:
            temptup = doGetEntrieOf(entrie)

            val1 += temptup[0]

            val2 += temptup[1]

            val3 += temptup[2]

    return val1, val2, val3

def doGetEntrieOf(entrie):

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