__author__ = 'uddipaan'
'''Some parts taken from sparse counts original code written by Shengjia'''

'''REVISIONS!!!'''

# test cnf file generated during solver is need to be made dynamic named.
# not quite sure if instance_id is needed or any time is needed


import random
import os


class SAT:
    def __init__(self,prb_nme):
    

        #here n denotes number of variables
        file_stream = open(prb_nme)
        head = file_stream.readline().split()
        self.n = int(head[2])

        

        self.clauses = []
        self.hashfnc = []
        #self.max_Xor = -1 ''' Set this to non-zero value to limit the maximum length of xor constraints
                              #If this length is exceeded, xor will be broken up into separate clauses'''
        self.newVar = 0

        while True:
            curline = file_stream.readline()
            if not curline:
                break
            self.clauses.append(curline.strip())
            self.no_of_clauses = len(self.clauses)

        print("There are " + str(self.n) + "variables and " + str(self.no_of_clauses) + "clauses")




    def hashfnc_generate(self,m,f):
        self.hashfncs = []
        self.newVar = 0

        self.max_Xor = -1

        cur_indx = self.n + 1

        for i in range(0,m):
            newfnc = []

            for X in range(1, self.n + 1):
                if random.random() < f:
                    newfnc.append(X)
                if random.randint(0,1) == 0:
                    newfnc[0] = -newfnc[0]
                    if self.max_Xor > 0:
                        while len(newfnc) > self.max_Xor:
                            temp = newfnc[0:self.max_Xor - 1]
                            newfnc = [cur_indx] + newfnc[self.max_Xor - 1:]
                            temp.append(cur_indx)
                            cur_indx += 1
                            self.newVar += 1
                            self.hashfncs.append(temp)
                    self.hashfncs.append(newfnc)

        print("Generated " + str(m) + "XOR constraints")
        if self.max_Xor > 0:
            print("Max Xor length is " + str(self.max_Xor) + ". Added " + str(self.newVar)+ "new variables!")
        







    def solver(self):
        os.mkdir("tmp")
        filename = "tmp/SAT_test.cnf"    #SAT_test.cnf needs to be made dynamic
        ofstream = open(filename, "w")
        ofstream.write("p cnf " + str(self.n + self.newVar) + " " + str(len(self.clauses) + len(self.hashfnc)) + "\n")


        for item in self.clauses:
            ofstream.write(item + "\n")
        for now_hashfnc in self.hashfncs:
            ofstream.write("x")
            for item in now_hashfnc:
                ofstream.write(str(item) + " ")
            ofstream.write("0\n")
        ofstream.close()
        solver = Command(['./cryptominisat', '--verbosity=0', '--gaussuntil=400', '--threads=1', filename])
        result = solver.run()
        run_command(['rm', filename])       #check

        result = result.split()
        if len(result) >= 2:
            outcome = result[1]
            if outcome == 'SATISFIABLE':
                return True
            elif outcome == 'UNSATISFIABLE':
                return False
        







def median(w):
    srt = sorted(w)
    print (srt)
    leng = len(srt)
    if not leng % 2:
        return int((srt[ leng // 2 ] + srt[ leng // 2 - 1]) // 2.0 )   # // is used in newer versions of python
    return int(srt[ leng // 2 ] )









