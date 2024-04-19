import pickle
import random

myFile = open("wordlist.txt","rt")

wordList = myFile.readlines()

def stringGenerator(x):
    str = ""
    for i in range(0,x):
        lineNumber = random.randint(0,wordList.__len__())
        str = str + wordList[lineNumber].strip('\n') + " "
    return str.strip(' ')

print(stringGenerator(3))