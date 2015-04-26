# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:48:14 2015

@author: phc
"""

""" 
							NON-PUNS HOMONYMS CREATION
				
"""	
import os		
from urllib import urlopen #To save information in a URL
import re   #Import regular expression library (Regex)
import numpy as np

""" -----------------------------Definitions------------------------------- """

def urlSave(url):   #Will save the information in a URL
    webPage = urlopen(url)
    return webPage			

""" -----------------------------Declarations------------------------------ """

websiteSource1 = 'http://dictionary.reference.com/browse/'#Name of website to get the sentences
websiteSource2 = 'http://www.thefreedictionary.com/'

homonymesFile = '/home/phc/Desktop/Dropbox/Hackapuns/hackapun/data/homophones.csv' #File containing the Homonymes
fileNameOutput = '/home/phc/Desktop/Non_puns_List.txt' #File that will contain the non-pun sentences
NONpunsFile = open(fileNameOutput,'w') 

homoPat = re.compile(r'(.*)(\n?)')	#Extract the homonyms
wordPat = re.compile(r'[^,]+')		#Extract each word in a 'homonym family'

words = []	#Will contain each words of each homonym
allSentences = [] #Will contain all the sentences

""" ---------------------------------Script-------------------------------- """

homonymesList = open(homonymesFile)
homonymesList = homonymesList.read()
homonymes = re.findall(homoPat,homonymesList) #Containes the list of homonymes 

	#The following loop will go through the homonymes and find a sentence in
	#the declared website containing each of the homonymes
for homo in homonymes:
	words = re.findall(wordPat,homo[0]) #Seperates word in each homonyms
	
	for word in words:
		print word
		url = websiteSource + word
		webPage = urlSave(url)
				
			
		exPatTXT = '(<span class="dbox-example">)(.*\s'+word+'\s.*?\.)(<\/span>)'
		exPat = re.compile(exPatTXT,re.I)	#Fnd the pattern of 'example sentences'
		
		sentences = re.findall(exPat,webPage.read())
			
		if any(sentences): #Only uses webpages that contains examples
			for sentence in sentences:
				if len(sentence[1]) >=25: #sentences with more than 25 carachters
					if len(re.findall('<.*',sentence[1])) == 0:
						allSentences.append(sentence[1]) 
						NONpunsFile.write(sentence[1]+'\n') #Write in a txt files
	
		
		
		
		







				