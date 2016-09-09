#! /usr/bin/python

def getStringsOfLines(fileName):
    source = open(fileName, 'rU')
    content = source.read()
    source.close()
    newList = content.split('\n')
    return newList #splits csv by newlines

def csvToDict(filename):
    listOfLines = getStringsOfLines(filename)
    dOL = {}
    for line in listOfLines:
        dataFromCSV = line.split(',')
#        print dataFromCSV
        userInfo = {}
        userInfo['password'] = dataFromCSV[1]
        userInfo['name'] = dataFromCSV[2]
        dOL[dataFromCSV[0]] = userInfo #turns to dictionary
    return dOL

