from __future__ import division, unicode_literals
import math
from textblob import TextBlob as tb
import os

def tf(word, blob):
    return blob.count(word) / len(blob)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if blob.find(word) != -1)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

if __name__ == '__main__':

    # bloblist

    for i, blob in enumerate(bloblist):
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:3]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))

########################################################33
