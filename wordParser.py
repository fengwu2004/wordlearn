lexicalEntries = 'lexicalEntries'

entries = 'entries'

senses = 'senses'

definitions = 'definitions'

examples = 'examples'

etymologies = 'etymologies'

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