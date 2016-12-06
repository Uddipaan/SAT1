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


#to execute the run_command in solver
def run_command(command):
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    return [item.strip() for item in iter(p.stdout.readline, b'')]










#to be used for solver where a command needs to be executed
class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None
        self.process_lock = threading.Lock()
        self.output = ""

    def run(self):
        
        def target():
            self.process_lock.acquire()
            if self.process is None:
                self.process = subprocess.Popen(self.cmd,
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.STDOUT)
                self.process_lock.release()
                self.output, err = self.process.communicate()
            else:
                self.process_lock.release()

        thread = threading.Thread(target=target)
        thread.start()
        
        if thread.is_alive():
            self.process_lock.acquire()
            if self.process is not None:
                try:
                    self.process.kill()
                except:
                    pass
            self.process = False
            self.process_lock.release()
            thread.join()
            return None
        return self.output










class SAT:
    def __init__(self,prb_nme):
    

        #here n denotes number of variables
        file_stream = open(prb_nme)
        head = file_stream.readline().split()
        self.n = int(head[2])

        

        self.clauses = []
        self.hashfnc = []
        self.max_Xor = -1 # Set this to non-zero value to limit the maximum length of xor constraints
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
	binLen=no_of_var + 2*numHash
	randBitsTotal = self.getBinary(binLen)
    	randBits=''
	print("randBitsTotal= "+str(randBitsTotal))
    	for i in range(self.n+1):
        	xorResult = 0
        	for j in range(numHash):
			print("randBitsTotal[i+j]= "+str(randBitsTotal[i+j]))
            		xorResult = xorResult^int(randBitsTotal[i+j])
			
        	randBits += str(xorResult)
    	return randBits



    def getBinary(self,binLen):
	byteLen = 1+binLen/8
    	_random_source = open("/dev/urandom","rb")
    	randBytes = _random_source.read(byteLen)
    	_random_source.close()

    	randInt = int(randBytes.encode("hex"),16)
    	randBin = bin(randInt).zfill(binLen)
    	return randBin[:binLen]







    def solver(self,finalFile):
	
	outputFileName = "tmp/file with var :"+str(self.n)+".cnf"
	cmd="./cryptominisat5  --verb=0 "+str(finalFile)+" > "+str(outputFileName)
	os.system(cmd)
	f = open(outputFileName,'r')
    	lines = f.readlines()
    	f.close() 
	#os.system('rm '+outputFileName)     can only be done after tested once
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
        print (srt)
        leng = len(srt)
        if not leng % 2:
            return int((srt[ leng / 2 ] + srt[ leng / 2 - 1]) / 2.0 )   # // is used in newer versions of python
        return int(srt[ leng / 2 ] )
        


