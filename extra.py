__author__ = 'uddipaan'


'''REVISIONS!!!'''

# test cnf file generated during solver is need to be made dynamic named.
# not quite sure if instance_id is needed or any time is needed

import subprocess, threading
import random
import os
import sys
import math
import re
import time







class SAT:
    def __init__(self,prb_nme):
    

        #here n denotes number of variables
        file_stream = open(prb_nme)
        head = file_stream.readline().split()
        self.n = int(head[2])

        

        self.clauses = []
        self.hashfnc = []
        self.max_Xor = -1    # Set this to non-zero value to limit the maximum length of xor constraints
                             # If this length is exceeded, xor will be broken up into separate clauses 
        self.newVar = 0


                    #NEED TO MAKE MECHANISM TO IGNORE 'C'->LEAST PRIORITY
                    
        while True:
            curline = file_stream.readline()
            if not curline:
                break
            self.clauses.append(curline.strip())
            self.no_of_clauses = len(self.clauses)

        print("There are " + str(self.n) + "variables and " + str(self.no_of_clauses) + "clauses")


    

        

    

    def addHash(self,initialFileName,finalFileName,m):			#numVariables=n numClauses=no_of_clauses
         numHash = m
    	 hashClauses = ''
    	 for i in range(int(numHash)):
		        	
		varNum = 0
        	randBits = self.findHashBits(numHash)#removed arg of no of var since object is invoked which can utilised all its attributes
        	hashClauses = hashClauses+'x'
        	needToNegate = False
        	if (randBits[0] == '1'):
            		needToNegate = True
        	for j in range(1, self.n+1):
			
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
   	 f.write('p cnf '+str(self.n)+' '+str(self.no_of_clauses+numHash)+'\n')
	 
    	 for line in lines:
        	f.write(str(line.strip())+'\n')
    	 if (numHash > 0):
        	f.write(hashClauses)
    	 f.close()
	 
		


    def findHashBits(self,numHash):
	no_of_var=self.n
	binLen=no_of_var + 2*numHash    #maybe for short; binLen = math.log(numHash)
	randBitsTotal = self.getBinary(binLen)
    	randBits=''
	
	randBitsTotal = randBitsTotal[:1]+randBitsTotal[2:] #the random bits were generating a 'b', so it is removed by considering only 								     after b
    	for i in range(self.n+1):
        	xorResult = 0
        	for j in range(numHash):
            		xorResult = xorResult^int(randBitsTotal[i+j])
			
        	randBits += str(xorResult)
    	return randBits



    def getBinary(self,binLen):
	byteLen = 1+binLen/8
    	_random_source = open("/dev/urandom","rb")
    	randBytes = _random_source.read(byteLen)
    	_random_source.close()

    	randInt = int(randBytes.encode("hex"),16)
    	randBin = format(randInt, 'b').zfill(binLen)
    	return randBin[:binLen]







    def solver(self,finalFile):
	
	outputFileName = "tmp/file_with_var_:"+str(self.n)+".txt"

	
	cmd="./cryptominisat5  --verb=0 "+str(finalFile)+" > "+str(outputFileName)
		
	os.system(cmd)
	f = open(outputFileName,'r')
    	lines = f.readlines()
    	f.close() 
	os.system('rm '+outputFileName)     
	res = lines[0]
	res_new = res.split()

	#print res_new[1]	 useless 
	 
	
	if not res_new:
		return 0
	else:
		if res_new[1] == 'SATISFIABLE':
                    return True
                elif res_new[1] == 'UNSATISFIABLE':
                    return False

    
def median(w):

    if not w:    
        return 0
    else:
        srt = sorted(w)
        
        leng = len(srt)
        if not leng % 2:
            return int((srt[ leng / 2 ] + srt[ leng / 2 - 1]) / 2.0 )   # // is used in newer versions of python
        return int(srt[ leng / 2 ] )
        


