from VectorSpace import VectorSpace
from tfidf import n_containing,tf
import util
import math
import os
import argparse

#numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def get_parser():
    parser = argparse.ArgumentParser(description='Query')
    parser.add_argument('--query', default='news')
    return parser


if __name__ == '__main__':

#    parser = get_parser()
#    args = parser.parse_args()

    #input data
    documents = []

    count = 0
    path = r"/mnt/c/Users/coil3/OneDrive/桌面/EnglishNews"
#    path = r"/home/coil3339/wsm/Project1/TestData"
    all_files = os.listdir(path) #得到資料夾下的所有檔名稱
    for fle in all_files: #遍歷資料夾
        if not os.path.isdir(fle): #判斷是否是資料夾，不是資料夾才開啟
            f = open(path+"/"+fle); #開啟檔案
            iter_f = iter(f); #建立迭代器
            string = ""
            for line in iter_f: #遍歷檔案，一行行遍歷，讀取文字
                string = string + line
            documents.append(string) #每個檔案的文字存到list中
            count += 1
            print(count)
#    print(documents) #列印結果

    vectorSpace = VectorSpace(documents)

#    print(vectorSpace.vectorKeywordIndex)

    # IDF    
    IDF = []
    for word in vectorSpace.vectorKeywordIndex.keys():
        IDF.append(math.log(len(documents) / (1 + n_containing(word, documents))))

    # Documents' TFIDF
    TFIDF = []
    for index in range(len(documents)):
        print("index = ",index)
        vector = []# * len(vectorSpace.vectorKeywordIndex)
        for word in range(len(vectorSpace.vectorKeywordIndex)):
            vector.append(vectorSpace.documentVectors[index][word] * IDF[word])
        TFIDF.append(vector)

    print("keyword len = ",len(vectorSpace.vectorKeywordIndex))

    queryString = [input("Input query: ")]
    querylist = vectorSpace.buildQueryVector(queryString)

    # Query's TFIDF
    Q_TFIDF = []
    for word in range(len(vectorSpace.vectorKeywordIndex)):
        Q_TFIDF.append(querylist[word] * IDF[word])
 
    # Cosine
#    ratings = vectorSpace.search(querylist,TFIDF)
    ratings = {}
    scorelist = util.cosine(TFIDF, Q_TFIDF)
    for i,newsID in enumerate(all_files):
        ratings[newsID] = scorelist[i]
    sorted_dic = sorted(ratings.items(),key = lambda x:x[1],reverse = True)
    ratings = dict(sorted_dic)

    print("TF-IDF Weighting + Cosine Similarity:")
    print("{:<20}".format("NewsID"),"score")
    for i,(k,v) in enumerate(ratings.items()):
        print("{:<20}".format(k),round(v))
        if i == 9:
            break

#    print(vectorSpace.vectorKeywordIndex)

#    print(vectorSpace.documentVectors)

#    print(vectorSpace.related(1))

#    print(vectorSpace.search(["cat"]))

###################################################
