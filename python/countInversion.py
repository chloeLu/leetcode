'''
Created on Jul 15, 2015

@author: nbkhzmb
'''
import sys
import os

def countInversion():
    intArray = []
    with open('file.txt') as f:
        for line in f:
            intArray.append(int(line))
    
    return countInv(intArray)[0]

def countInv(intArray):
    # border case: intArray size is 1 or 2
    if len(intArray) == 1:
        return (0, intArray)
    elif len(intArray) == 2:
        if intArray[0] > intArray[1]:
            return (1, intArray[::-1])
        else:
            return (0, intArray)
    
    len1 = len(intArray) / 2
    len2 = len(intArray) - len1
    result1 = countInv(intArray[0:len1])
    result2 = countInv(intArray[len1:])
    
    count = result1[0] + result2[0]
    intArr1 = result1[1]
    intArr2 = result2[1]
    sortedIntArray = []
    # merge
    i = 0
    j = 0
    while i < len1 and j < len2:
        if intArr1[i] > intArr2[j]:
            sortedIntArray.append(intArr2[j])
            j += 1
            count += (len1 - i)
        else:
            sortedIntArray.append(intArr1[i])
            i += 1
    if i < len1:
        sortedIntArray.extend(intArr1[i:])
    else:
        sortedIntArray.extend(intArr2[j:])
    return (count, sortedIntArray)

def test11():
    arr = [3,7,1,6,4,2,5]
    result = countInv(arr)
    print "result: " + str(result[0])
    
def test111():
    print os.getcwd()
