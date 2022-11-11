import json
import random
from os import walk

#class common:
@staticmethod
def saveToJSON(char):
    File = open("Generated/" + char["Name"] + ".json", "w", encoding='iso-8859-15')
    enc = json.JSONEncoder().encode(char)
    parsed = json.loads(enc)
    File.write(json.dumps(parsed, indent=4, ensure_ascii=False))
    File.close()

@staticmethod
def getListFile(location):
    f = open(location, "r", encoding='iso-8859-15')
    splitList = f.read().split("\n")
    f.close()
    return splitList

# out of 100
@staticmethod
def traitMeasure(x):
    if x < 10:
        return "Not at all"
    elif x < 20:
        return "Nearly not at all"
    elif x < 30:
        return "Very little"
    elif x < 40:
        return "A Little"
    elif x < 50:
        return "Fairly"
    elif x < 60:
        return "Reasonably"
    elif x < 70:
        return "Considerably"
    elif x < 80:
        return "Very"
    elif x < 90:
        return "Really very"
    else:
        return "Extremely"

# 1/chance to change to random from list
# otherwise return normal 
@staticmethod
def possibleAlteration(chance, normal, list):
    if random.randint(1,chance) != 1:
        return normal
    else:
        return list[random.randint(0,len(list)-1)]

# find possible file in folder
# if no return default
@staticmethod
def findFile(folder, findFile, default):
    #list of all files in folder
    f = []
    for (dirpath, dirnames, filenames) in walk(folder):
        f.extend(filenames)
        break

    #get relevant
    toReturn = []
    for file in f:
        if findFile == file:
            toReturn = getListFile(folder + "/" + findFile)
    
    if len(toReturn) < 1:
        toReturn = getListFile(folder + "/" + default)
    
    return toReturn

@staticmethod
def findFilesInRange(folder, range):
    #list of all files in folder
    f = []
    for (dirpath, dirnames, filenames) in walk(folder):
        f.extend(filenames)
        break

    #add files to list if within/under range
    possibleFiles = []
    for file in f:
        if range >= int(file):
            possibleFiles.append(file)

    #add jobs from those files to list
    toReturn = []
    for file in possibleFiles:
        toReturn.extend(getListFile(folder + file))
    
    return toReturn


# returns random from list
# simple but used a lot
@staticmethod
def getRandom(list):
    return list[random.randint(0,len(list)-1)]

# for twoPart pieces Eg 'Younger' 'Sister'
@staticmethod
def returnMultipleTwoPart(x, listA, listB):
    toReturn = []
    while x > 0:
        toReturn.append(getRandom(listA) + " " + getRandom(listB))
        x = x - 1
    return toReturn

# for finite lists, popped
@staticmethod
def returnMultiple(x, list, dep=1):
    listCopy = list
    toReturn = []
    while x > 0:
            toReturn.append(listCopy.pop(random.randint(0,len(listCopy)-1)))
            x = x - dep
    return toReturn

