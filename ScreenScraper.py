#!/usr/bin/env Python

#   ------------------------------------------------------------------------------------------
#   NAME:    J. Murray
#   DATE:    10/29/2016
#   PURPOSE: Implementation for Screen Scraping Monster Class Info


#   v0.1:   10/29/2016 (JBM) - Initial Version. Scraping Base Attributes of Monsters
#   ------------------------------------------------------------------------------------------
from urllib.request import urlopen
#import html5lib

#with urlopen("http://www.puzzledragonx.com/en/monster.asp?n=2998") as f:
#    document = html5lib.parse(f, transport_encoding=f.info().get_content_charset())

from bs4 import BeautifulSoup

#page = urllib.request.urlopen('http://www.puzzledragonx.com/en/monster.asp?n=148')

def ScrapeInfo(url):
#try:
    #page = urlopen('http://www.puzzledragonx.com/en/monster.asp?n=148')
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

    import string
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
                        print(k,separator,end="")
                        retList.append(k)
                else:
                    if set(j).issubset(printset):
                        print(j,separator,end="")
                    else:
                        print("UNPRINTABLE",separator,end="")

                #print("->",str(j))
                    #print(j,separator,end="")
                    retList.append(j)
        else:
            print(separator,end="")#print("Skipping - JAPANESE Characters")

    print()
    soup.decompose()
#    page.decompose()
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



try:

    #monsterList = list(range(1931,3252+1))
    #ex = [  1340,1341,1708,1892,1893,1894,1895,2573,2897,2898,
    #        3188,3189,3190,3191,3192,3193,3194,3207,3208,3209,
    #        3211,3212,3214,3216,3244,3245,3248]


    #for i in ex:
    #    try:
    #        monsterList.remove(i)
    #    except ValueError as v:
    #        print(i," - Not in the List!")

    monsterList = [3209,3212,3214,3244,3245,3248,3253,3254,3255,3256,3257,3258,3259,3267,3268]
    print("Size of list:",len(monsterList))

    baseURL = 'http://www.puzzledragonx.com/en/monster.asp?n='
    totalList = dict()



    for i in monsterList:#range(1,100):
        print(i,'|',end="")
        newItem = ScrapeInfo(baseURL+str(i))
        totalList[i] = newItem

    print(totalList)

except Exception as e:
    
    print("Caught the following: ",e)    

    input()

