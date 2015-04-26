import nltk
from stemmingSentence import *

def processSentence(sentence):

    # Stemming Sentence
    sentWithoutSymbols = stemmingSentence(sentence)

    # Tokenizing sentence (splitting sentence)
    tokens = nltk.word_tokenize(sentWithoutSymbols)

    return tokens


sent_brok = processSentence("The magician got so mad he pulled his hare out")