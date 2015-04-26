import csv
import os
from subprocess import call

import argparse

parser = argparse.ArgumentParser(description='download and process google files')
parser.add_argument('letter',help='first letter of type')

args = parser.parse_args()
letter = args.letter

def addPair(result, word1, word2, score):
        i1 = word1.find("_")
        if i1 > -1 and i1 < 3: return
        if i1 > -1: word1 = word1[:i1]

        i2 = word2.find("_")
        if i2 > -1 and i2 < 3: return
        if i2 > -1: word2 = word2[:i2]

        if not word1 in result:
            result[word1] = {word2: score}
        elif not word2 in result[word1]:
            result[word1][word2] = score
        else: result[word1][word2] += score
os.chdir("../pydata")

def parse(name):
    print("PARSING", name)

    result = {}

    MIN_LENGTH = 2;


    def valid(word):
        if '$' in word or '.' in word or '/' in word or 'NUM' in word:
            return False
        return True

    i = 0
    LIMIT = 2 * 1000 * 1000 * 1000

    call(["rm", "googlebooks-eng-all-3gram-20120701-"+name+".gz"])
    call(["rm", "googlebooks-eng-all-3gram-20120701-"+name])
    call(["rm", "googlebooks-eng-all-3gram-20120701-"+name+"_results.csv"])
    call(["wget", "http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-3gram-20120701-"+name+".gz"])
    call(["gunzip", "googlebooks-eng-all-3gram-20120701-"+name+".gz"])

    with open("googlebooks-eng-all-3gram-20120701-"+name) as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"):
            if i > LIMIT:
                break
            i = i + 1;
            ngram = line[0].split()

            l0 = len(ngram[0])
            l1 = len(ngram[1])
            l2 = len(ngram[2])

            match_count = int(line[2])

            if valid0 and valid1 and l0 > MIN_LENGTH and l1 > MIN_LENGTH:
               addPair(result, ngram[0], ngram[1], match_count)
            if valid1 and valid2 and l1 > MIN_LENGTH and l2 > MIN_LENGTH:
               addPair(result, ngram[1], ngram[2], match_count)
            if valid0 and valid2 and l0 > MIN_LENGTH and l2 > MIN_LENGTH:
               addPair(result, ngram[0], ngram[2], match_count)


    # save
    save = True
    if save:
        with open('googlebooks-eng-all-3gram-20120701-'+name+'_result.csv', 'w') as fp:
            a = csv.writer(fp, delimiter=',')

            for key in result:
                item = result[key]
                data = []
                for itemkey in item:
                    data.append([key, itemkey, item[itemkey]])
                a.writerows(data)

    call(["rm", "googlebooks-eng-all-3gram-20120701-"+name])
    #print(result)

for c in "_abcdefghijklmnopqrstuvwxyz":
    parse(letter+c)
