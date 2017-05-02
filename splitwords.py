from pymongo import MongoClient
import createExcel
import urllib.request
import os

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


def getTotalWord():
    
    client = MongoClient('localhost', 27017)
    
    db = client["test"]
    
    coll = db['totalwords']
    
    totals = coll.find({})
    
    client.close()
    
    results = []
    
    for result in totals:
        
        results.append(result)
    
    return results

def saveMp3(items, path):
    
    for item in items:
    
        if 'lexicalEntries' in item:
        
            if 'pronunciations' in item['lexicalEntries'][0]:
            
                if 'audioFile' in item['lexicalEntries'][0]['pronunciations'][0]:
                    
                    result = {'id': item['id'], 'url': item['lexicalEntries'][0]['pronunciations'][0]['audioFile']}

                    print(result['url'])
                    
                    request = urllib.request.urlopen(result['url'], timeout = 10)
                
                    with open(path + result['id'] + '.mp3', 'wb') as f:
                        
                        try:
                            f.write(request.read())
                        
                        except:
                            
                            print("error")


def mkdir(path):
    # 引入模块

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print
        path + ' 创建成功'
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print
        path + ' 目录已存在'
        return False


def run():

    needReviewWords = getTotalWord()

    index = 0
    
    result = []
    
    for word in needReviewWords:
        
        result.append(word)
        
        if len(result) > 200:
            
            path = '/Users/yan/code/%d/' % index

            excelpath = path + 'word.xlsx'

            index += 1
            
            mkdir(path)
            
            createExcel.instance().toExcel(result, excelpath)

            # saveMp3(result, path)

            result.clear()
               
run()

print('完毕')