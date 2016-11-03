#!/usr/bin/env Python

#   ------------------------------------------------------------------------------------------
#   NAME:    J. Murray
#   DATE:    10/29/2016
#   PURPOSE: Implementation for Screen Scraping Monster Class Info

#   v0.1:   10/29/2016 (JBM) - Initial Version. Scraping Base Attributes of Monsters
#   v0.2:   11/02/2016 (JBM) - Adding functionality to scrape Active / Leader Skill
#                            - Fixed ' ' Injection for Scripts (sep='')
#   v0.3:   11/03/2016 (JBM) - Added Overall Execution Time stats and Exit Key Function

#   TODO LIST:
#
#   - FIX MEMORY UTILIZATION (SOUPSTRAINER MAY WORK)
#   - OUTPUT TO CSV / XLSX FILE (FIXED FILE NAME & LOCATION)
#   - FIX ROW FORMATTING FOR:   MONSTER BASE ATTRIBUTE SPACING & ACTIVE/LEADER SKILL SCRAPING
#   - ADD TIMING TO FIND RUNTIME FOR SCRIPT (TO UNDERSTAND TIME ASSOCIATED WITH SCRAPING)       - (DONE!)
#   - PRESS 'Q' TO QUIT (AS OPPOSED TO KEYBOARD MASHING THAT OCCURS NOW - PROTECTS RUN STATS)   - (DONE!)
#   - ADD UNICODE/PAGE SUPPORT FOR JAPANESE CHARACTERS, AND REMOVE THE 'UNPRINTABLE' MESSAGE
#   - FIX EXCEPTION REMOVES AT START, AND CLARIFY MESSAGES ('THESE WERE OMITTED, THESE WERE NOT IN THE RANGE, ETC')
#   ------------------------------------------------------------------------------------------

from urllib.request import urlopen
from bs4 import BeautifulSoup
#------
import string

def ScrapeBaseInfo(url):

    page = urlopen(url)
    pageContent = page.read()

    soup = BeautifulSoup(pageContent, 'html5lib')

    #results = soup.find_all('compareprofile')
    #yes = soup.body.div
    #inputTag = soup.find_all(attrs={"name": "Rarity"})
    #inputTags = soup.find_all(attrs={"id": "compareprofile"})


    #inputTags = soup.find_all(attrs={"class": "ptitle"})   #--These are the kids!
    #inputTags = soup.find_all(attrs={"id": "compareprofile"}) 

    #import sys
    #import codecs
    #sys.stdout = codecs.getwriter('utf8')(sys.stdout)
    #sys.stderr = codecs.getwriter('utf8')(sys.stderr)

    inputTags = soup.find_all(attrs={"class": "data"})

    #for i in inputTags:
    ##    print("Contents Type:",type(i.contents))
    ##    print("Contents Length:", len(i.contents))
    ##    print("Contents [0] Type:",type(i.contents[0]))
    ##    print("Class:",i.attrs)
    ##    print(type(i.attrs))
    #    if "jap" not in i.attrs.get("class"):
    #        print("North America")
    #    else:
    #        print("JAP!")
    #print()

    separator = '|'
    print("Total Attributes: ",len(inputTags),separator,end="")

    retList = []

    printset = set(string.printable)

    for i in inputTags:

        if "jap" not in i.attrs.get("class"):
        
            for j in i.children:
                if not isinstance(j,str):
                    for k in j:
                        print(k,separator,end="",sep='')
                        retList.append(k)
                else:
                    if set(j).issubset(printset):
                        print(j,separator,end="",sep='')
                    else:
                        print("UNPRINTABLE",separator,end="",sep='')

                #print("->",str(j))
                    #print(j,separator,end="")
                    retList.append(j)
        else:
            print(separator,end="",sep='')#print("Skipping - JAPANESE Characters")

    print()
    soup.decompose()

    return retList

#except as e:
#    print(e)
#    pass

    ##   Monster Name
    #for i in inputTags[0].children:
    #    #if i != 1:
    #    #    pass
    #    print(i)

    ##   Monster Name (JP)
    #for i in inputTags[1].children:
    #    #if i != 1:
    #    #    pass
    #    for j in i:
    #        print(type(j),end="")
    #        printset = set(string.printable)
    #        #print(string.printable)
        
    #        if set(j).issubset(printset):
    #            print(j)
    #        else:
    #            print("UNPRINTABLE")
    #        #print("->",str(j))



    #-------------------------------------------------------------------------

    ##   Monster Name
    #for i in inputTags[0].children:
    #    #if i != 1:
    #    #    pass
    #    print(i)

    ##   Monster Name (JP)
    #for i in inputTags[1].children:
    #    #if i != 1:
    #    #    pass
    #    for j in i:
    #        print(type(j),end="")
    #        printset = set(string.printable)
    #        #print(string.printable)
        
    #        if set(j).issubset(printset):
    #            print(j)
    #        else:
    #            print("UNPRINTABLE")
    #        #print("->",str(j))

    ##   Material Type
    #for i in inputTags[2].children:
    #    #print(i)
    #    for j in i:
    #        print(type(j),end="")
    #        print("->",j,"(Printable)" if set(j).issubset(printset) == True else "(UnPrintable)")

    ##   ?
    #for i in inputTags[3].children:
    #    #print(i)
    #    for j in i:
    #        print(type(j),end="")
    #        print("->",j,"(Printable)" if set(j).issubset(printset) == True else "(UnPrintable)")

    ##   ?
    #for i in inputTags[4].children:
    #    #print(i)
    #    for j in i:
    #        print(type(j),end="")
    #        print("->",j,"(Printable)" if set(j).issubset(printset) == True else "(UnPrintable)")

    #for i in inputTags[5].children:
    #    #print(i)
    #    for j in i:
    #        print(type(j),end="")
    #        print("->",j,"(Printable)" if set(j).issubset(printset) == True else "(UnPrintable)")

    #for i in inputTags[6].children:
    #    #print(i)
    #    for j in i:
    #        print(type(j),end="")
    #        print("->",j,"(Printable)" if set(j).issubset(printset) == True else "(UnPrintable)")

    #for i in inputTags[7].children:
    #    #print(i)
    #    for j in i:
    #        print(type(j),end="")
    #        print("->",j,"(Printable)" if set(j).issubset(printset) == True else "(UnPrintable)")

    #import string

    #printset = set(string.printable)
    #print(string.printable)
    #for i in inputTags:
    #    #if set(i).issubset(printset):
    #    #    print(i)
    #    #else:
    #    #    print("UNPRINTABLE")
    #    for j in i.children:


    #        print(type(j))
    #        if set(i).issubset(printset):
    #            print(i)
    #        else:
    #            print("UNPRINTABLE")

    #print(pageContent) #--SWEET MERCIFUL JEEBUS, WHAT DID THEY BUILD THIS WITH??!!?




def ScrapeSkillInfo(url):

    page = urlopen(url)
    pageContent = page.read()

    soup = BeautifulSoup(pageContent, 'html5lib')

    #inputTags = soup.find_all(attrs={"class": "ptitle"})   #--These are the kids!
    #inputTags = soup.find_all(attrs={"id": "compareprofile"}) 

    inputTags = soup.find_all(attrs={"class": "blue"})

    #for i in inputTags:
    ##    print("Contents Type:",type(i.contents))
    ##    print("Contents Length:", len(i.contents))
    ##    print("Contents [0] Type:",type(i.contents[0]))
    ##    print("Class:",i.attrs)
    ##    print(type(i.attrs))
    #    if "jap" not in i.attrs.get("class"):
    #        print("North America")
    #    else:
    #        print("JAP!")
    #print()

    separator = '|'
    print("Total Attributes: ",len(inputTags),separator,end="",sep='')

    retList = []

    printset = set(string.printable)

    for i in inputTags:

        if "jap" not in i.attrs.get("class"):
        
            for j in i.children:
                if not isinstance(j,str):
                    for k in j:
                        print(k,separator,end="",sep='')
                        retList.append(k)
                else:
                    if set(j).issubset(printset):
                        print(j,separator,end="",sep='')
                    else:
                        print("UNPRINTABLE",separator,end="",sep='')

                #print("->",str(j))
                    #print(j,separator,end="")
                    retList.append(j)
        else:
            print(separator,end="",sep='')#print("Skipping - JAPANESE Characters")

    inputTags = soup.find_all(attrs={"class" : "green"})
    for i in inputTags:

        if "jap" not in i.attrs.get("class"):
        
            for j in i.children:
                if not isinstance(j,str):
                    for k in j:
                        print(k,separator,end="",sep='')
                        retList.append(k)
                else:
                    if set(j).issubset(printset):
                        print(j,separator,end="",sep='')
                    else:
                        print("UNPRINTABLE",separator,end="",sep='')

                #print("->",str(j))
                    #print(j,separator,end="")
                    retList.append(j)
        else:
            print(separator,end="",sep='')#print("Skipping - JAPANESE Characters")

    print()
    soup.decompose()

    return retList

#------------------------------------------------------------------------------------------
#   MAIN FUNCTION - IMPLEMENTATION

import datetime

try:

    startingID = input("Starting ID:\t")
    
    assert(int(startingID) and int(startingID) < 3268)
    startingID = int(startingID)

    totalAmt =  input("How Many:\t")
    if totalAmt is "":
        totalAmt = (3268 - startingID)
    assert(int(totalAmt) and int(totalAmt)+startingID <= 3268)
    
    totalAmt = int(totalAmt)

    startTime = datetime.datetime.now()  #Start Time for Script
    print()
    print('Start Time:',startTime.time(),'\n')

    monsterList = list(range(startingID,totalAmt+startingID+1))
    ex = [  1340,1341,1708,1892,1893,1894,1895,2573,2897,2898,
            3188,3189,3190,3191,3192,3193,3194,3207,3208,
            3211,3216,3260,3261,3262,3263,3264,3265,3266]


    omitList = []
    for i in ex:
        try:
            monsterList.remove(i)
        except ValueError as v:
            #print(i," - Not in the List!")
            omitList.append(i)

    if len(omitList):
        print("Omitted the following values: ",omitList)

    #monsterList = [3209,3212,3214,3244,3245,3248,3253,3254,3255,3256,3257,3258,3259,3267,3268]

    print("Size of list:",len(monsterList),'\n')

    baseURL = 'http://www.puzzledragonx.com/en/monster.asp?n='
    totalList = dict()

    for i in monsterList:
        print(i,'|',end="")
        newItem = ScrapeSkillInfo(baseURL+str(i))
        totalList[i] = newItem

    #print(totalList)   - Trying to print unencodeable characters (FIX WITH UNICODE SUPPORT) TODO: FIX IT!
    
except AssertionError as a:
    
    print("Sorry, please select a valid value!")

except Exception as e:
    
    print("Caught the following: ",e)

    
stopTime = datetime.datetime.now()  #Start Time for Script  
print()
print('End Time:',stopTime.time())
print("Total Execution Time: ",stopTime - startTime,'\n')


print(r"Press 'q' or 'Q' to continue")
ui = ''
while ui != 'q' and ui != 'Q':
    ui = input()