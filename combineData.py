import csv
import os

skipped = 0
added = 0

#os.chdir("./pydata")

def addPair(result, word1, word2, score):
    l1 = len(word1)
    l2 = len(word2)
    
    if l1 < 2 or l2 <2:
        #skipped = skipped +1
        return
    
    if not word1 in result:
        result[word1] = {word2: score}
    #added = added + 1
    elif not word2 in result[word1]:
        result[word1][word2] = score
    #added = added + 1
    else: result[word1][word2] += score


result = {};

with open('pairs.csv') as file:
    for line in csv.reader(file):
        addPair(result, line[0], line[1], int(line[2]))


with open('pairs_clean.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    
    for key in result:
        item = result[key]
        data = []
        for itemkey in item:
            data.append([key, itemkey, item[itemkey]])
        a.writerows(data)

