# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:34:52 2015
@author: phc

									PUNS EXTRACTION FOR punoftheday.com
						Takes out all the puns since 1996 on www.punoftheday.com
						and save them in a texte file (filenameOutput).


"""

from urllib import urlopen #To save information in a URL
import re   #Import regular expression library (Regex)
import numpy as np

def urlSave(url):   #Will save the information in a URL
    webPage = urlopen(url)
    return webPage


# Regex for email pattern. Ignorecase flag as to be on for it to work
punPat = re.compile(r'(<td>[1-9]+\.<\/td>\s*<td>)(.*?)(<.*)',re.I) 
fileNameOutput = '/home/phc/Desktop/punsList.txt'
punsFile = open(fileNameOutput,'w')       #Creates the file with the name in fileNameOutput				
urlBase = 'http://www.punoftheday.com/cgi-bin/disppuns.pl?cat=' #Core part of the URL

allPuns = []
"""----------------------------------  SCRIPT ------------------------------"""


for year in range(1996,2016):
	
	print 'Extracting puns of ' + str(year)

	for month in range(1,13):
		firstPunPage = []
		
		page= 0
		stop = 0
		
		while stop == 0:
			page += 1		
					
			url = urlBase + str(month) + '&sub=' + str(year) +'&ord=M&page=' + str(page)	#Url of the page
			webPage = urlopen(url)		#Loads the page 
			punsList = re.findall(punPat,webPage.read())	#find the puns in the page
			
			if len(punsList) == 0:
				break
			
			if page==1:	#Will save the first pun of each pages to make sure page is new
				firstPunPage = punsList[0][1]
			else:
				if firstPunPage == punsList[0][1]: #will make the while loop stop is true
					stop = 1 
			
			if stop == 0:
				for pun in punsList:
					allPuns.append(pun[1]) 
					punsFile.write(pun[1]+'\n')

punsFile.close()



    
    
    
    
    