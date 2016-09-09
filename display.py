#! /usr/bin/python
print "content-type: text/html\n"

import cgitb
cgitb.enable()

import cgi
fromQS = cgi.FieldStorage()

# from code from period 6

def getStringsOfLines( fileName):
    f = open( fileName, 'rU')
    oneString = f.read()
    f.close()
    listOfLines = oneString.split( '\n')
    return listOfLines

stringsOfLines = getStringsOfLines('accounts.csv')
titles = stringsOfLines.pop(0).split(',')
 
def getDictionaryOfLines( listOfLines):
    dOL = {}
    for line in listOfLines:
        fieldList = line.split(',')
        nonIdFields = {}
        curField = 1
        while curField < len( fieldList):
            nonIdFields[ titles[curField]] = fieldList[ curField]
            curField += 1
        dOL[ fieldList[0]] = nonIdFields
    return dOL

userandpass = getDictionaryOfLines (stringsOfLines)

listofKeys = []
for key in userandpass:
	listofKeys.append(key)

if fromQS['username'].value in listofKeys == True and fromQS['password'].value == userandpass[fromQS['username'].value]['password']:
	print 'Hello' , userandpass[fromQS['username'].value]['owner']
else: 
	print 'Hello'
