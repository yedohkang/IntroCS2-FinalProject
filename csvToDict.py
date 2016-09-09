def getStringsOfLines(fileName):
    source = open(fileName, 'rU')
    content = source.read()
    source.close()
    newList = content.split('\n')
    return newList

def csvToDict(filename):
    listOfLines = getStringsOfLines(filename)
    metaData = listOfLines.pop(0)
    titles = metaData.split(',')
    dOL = {}
    for line in listOfLines:
        fieldList = line.split(',')
        nonIdFields = {}
        curField = 1
        while curField < len(fieldList):
            try:
                float(fieldList[curField])
                nonIdFields[titles[curField]] = float(fieldList[curField])
            except ValueError: 
                nonIdFields[titles[curField]] = fieldList[curField]
            curField += 1
        dOL[fieldList[0]] = nonIdFields
    return dOL

#print csvToDict (fileName)

