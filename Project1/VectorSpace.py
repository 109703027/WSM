from pprint import pprint
from Parser import Parser
import util
import os
import argparse
import re
import string

class VectorSpace:
    """ A algebraic model for representing text documents as vectors of identifiers. 
    A document is represented as a vector. Each dimension of the vector corresponds to a 
    separate term. If a term occurs in the document, then the value in the vector is non-zero.
    """

    #Collection of document term vectors
    documentVectors = []

    #Mapping of vector index to keyword
    vectorKeywordIndex=[]

    #Tidies terms
    parser=None


    def __init__(self, documents=[]):
        self.documentVectors=[]
        self.parser = Parser()
        if(len(documents)>0):
            self.build(documents)

    def build(self,documents):
        """ Create the vector space for the passed document strings """
        self.vectorKeywordIndex = self.getVectorKeywordIndex(documents)
        self.documentVectors = [self.makeVector(document) for document in documents]

        #print(self.vectorKeywordIndex)
        #print(self.documentVectors)


    def getVectorKeywordIndex(self, documentList):
        """ create the keyword associated to the position of the elements within the document vectors """

        #Mapped documents into a single word string	
        vocabularyString = " ".join(documentList)

        vocabularyList = self.parser.tokenise(vocabularyString)
        #Remove common words which have no search value
        vocabularyList = self.parser.removeStopWords(vocabularyList)
        uniqueVocabularyList = util.removeDuplicates(vocabularyList)

        vectorIndex={}
        offset=0
        #Associate a position with the keywords which maps to the dimension on the vector used to represent this word
        for word in uniqueVocabularyList:
            vectorIndex[word]=offset
            offset+=1
        return vectorIndex  #(keyword:position)


    def makeVector(self, wordString):
        """ @pre: unique(vectorIndex) """

        #Initialise vector with 0's
        vector = [0] * len(self.vectorKeywordIndex)
        wordList = self.parser.tokenise(wordString)
        wordList = self.parser.removeStopWords(wordList)
        for word in wordList:
            vector[self.vectorKeywordIndex[word]] += 1; #Use simple Term Count Model
        return vector


    def buildQueryVector(self, termList):
        """ convert query string into a term vector """
        query = self.makeVector(" ".join(termList))
        return query


    def related(self,documentId):
        """ find documents that are related to the document indexed by passed Id within the document Vectors"""
        ratings = [util.cosine(self.documentVectors[documentId], documentVector) for documentVector in self.documentVectors]
        #ratings.sort(reverse=True)
        return ratings


    def search(self,searchList,TFIDF):
        """ search for documents that match based on a list of terms """
        queryVector = self.buildQueryVector(searchList)

        ratings = {}
        for i,documentVector in enumerate(TFIDF):
            index = "News" + str(i+1) + ".txt"
            ratings[index] = util.cosine(queryVector, documentVector)
        sorted_dic = sorted(ratings.items(),key = lambda x:x[1],reverse = True)
        ratings = dict(sorted_dic)
        #ratings.sort(reverse=True)
        return ratings

if __name__ == '__main__':

#    parser = get_parser()
#    args = parser.parse_args()

    #input data
    documents = []

    i = 0
#    path = r"/mnt/c/Users/coil3/OneDrive/桌面/EnglishNews"
    path = r"/home/coil3339/wsm/Project1/testData"
    all_files = os.listdir(path)
    for fle in all_files:
        # open the file and then call .read() to get the text
        with open(os.path.join(path, fle),"rb") as f:
            text = str(f.read())
            text = text.replace(r"\n","")
            text = text.replace(r"/"," ")
            for j in r"!#$%&'()*+,.:;<=>?@[\]^_`{|}~’＂‵":
                text = text.replace(j,"")
            print(text)
            documents.append(text)
            i += 1
            print(i)

    vectorSpace = VectorSpace(documents)

    print(vectorSpace.vectorKeywordIndex)

    print(vectorSpace.documentVectors)

    print(vectorSpace.related(1))

#    print(vectorSpace.search(["cat"]))

###################################################
