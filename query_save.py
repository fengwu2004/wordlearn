# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import totalwords
import wordParser

app_id = '880d5e0b'

app_key = 'c70b0ad322cc9cd89227b289585952a3'

def run(lines):

    results = []

    for line in lines:

        if totalwords.instance().checkExist(line):

            continue

        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + 'en' + '/' + line.lower()

        r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key, "Accept":"application/json"})

        try:
            temp = r.json()
        except:
            print("异常")
        else:
            results.append(temp)

    saveToTotal(results)

from pymongo import MongoClient

def saveToTotal(results):

    if len(results) == 0:

        return

    count = totalwords.instance().results.count()

    tempItems = []

    for unit in results:

        item = unit['results'][0]

        item['index'] = count

        tup = wordParser.getEntrieOf(item)

        item['def'] = tup[0]

        item['exam'] = tup[1]

        item['ety'] = tup[2]

        tempItems.append(item)

        count += 1

    totalwords.instance().save(tempItems)