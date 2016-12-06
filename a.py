import sys
import os
import math
import re
import random
import time



def main():

	



	def getBinary(binLen):
    		byteLen = 1+binLen/8
    		_random_source = open("/dev/urandom","rb")
    		randBytes = _random_source.read(byteLen)
    		_random_source.close()

    		randInt = int(randBytes.encode("hex"),16)
    		randBin = bin(randInt).zfill(binLen)
    		return randBin[:binLen]



	def findHashBits(numHash):
    		numVariables=10
    		randBitsTotal = getBinary(numVariables+2*numHash)
    		randBits=''
    		print("randBitsTotal= "+str(randBitsTotal))
    		for i in range(numVariables+1):
        		xorResult = 0
        		for j in range(numHash):
            			xorResult = xorResult^int(randBitsTotal[i+j])
        		randBits += str(xorResult)
    		return randBits






