from processSentence import *

sent_brok = processSentence("The magician got so mad he pulled his hare out")

#print sent_brok

"""
def sentFeat(sent):
    # Preprocessing the sentence
    sent_brok = processSentence(sent)
    # Looking whether sentence have homonym or not
    for word in sent_brok:
        for homWord in homonym:
            if homWord[1] == word:
            # search(ngram, word)
# how to get frequency




# searching ngram frequency for a word
def search(ngram_Corpus, searchFor):
    for key in ngram_Corpus:
        for value in ngram_Corpus[k]:
            if searchFor in value:
                return key
    return None


"""