import sys
import os
import math
import re
import random
import time


# This will add hash to the initial File with numHash of XOR clauses! 
def addHash(initialFileName,finalFileName,numVariables,numClauses,m):
    numHash = m
    hashClauses = ''
    for i in range(int(numHash)):
        varNum = 0
        randBits = findHashBits(numVariables,numHash)
        hashClauses = hashClauses+'x'
        needToNegate = False
        if (randBits[0] == '1'):
            needToNegate = True
        for j in range(1, numVariables+1):
            if (randBits[j] == '1'):
                varNum = varNum+1
                if (needToNegate):
                    hashClauses = hashClauses+'-'
                    needToNegate = False
                hashClauses = hashClauses+str(j)+' '
        hashClauses = hashClauses+' 0\n'
    f = open(initialFileName,'r')
    lines = f.readlines()
    f.close()
    f = open(finalFileName,'w')
    f.write('p cnf '+str(numVariables)+' '+str(numClauses+numHash)+'\n')
    for line in lines:
        f.write(str(line.strip())+'\n')
    if (numHash > 0):
        f.write(hashClauses)
    f.close()

def findHashBits(numVariables,numHash):
    randBitsTotal = getBinary(numVariables+2*numHash)
    randBits=''
    for i in range(numVariables+1):
        xorResult = 0
        for j in range(numHash):
            xorResult = xorResult^int(randBitsTotal[i+j])
        randBits += str(xorResult)
    return randBits

def getBinary(binLen):
    byteLen = 1+binLen/8
    _random_source = open("/dev/urandom","rb")
    randBytes = _random_source.read(byteLen)
    _random_source.close()

    randInt = int(randBytes.encode("hex"),16)
    randBin = bin(randInt).zfill(binLen)
    return randBin[:binLen]
