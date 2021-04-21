import os
import string
from collections import OrderedDict

import numpy as np


def letters_counter(text):
    all_freq = {}
    alphabet = list(string.ascii_lowercase)

    for i in text:
        for j in alphabet:
            if j == i:
                if i in all_freq:
                    all_freq[i] += 1
                else:
                    all_freq[i] = 1
    all_freq = OrderedDict(sorted(all_freq.items()))
    return all_freq


def to_vector(dict):
    vec = list()
    for key, value in dict:
        vec.append(value)
    a = np.array(vec)
    print(a)
    return a

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


dirName = 'Train'
listOfFiles = getListOfFiles(dirName)

for elem in listOfFiles:
    with open(elem, "r", encoding="utf8") as file:
        data = file.read().replace('\n', '')
    vec = to_vector(letters_counter(data).items())
    print(vec/np.linalg.norm(vec))