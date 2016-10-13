__author__ = 'uddipaan'


import random



class SAT:
    def __init__(self,prb_nme)
    

        #here n denotes number of variables
        file_stream = open(prb_nme)
        head = file_stream.readline().split()
        self.n = int(head[2])

        print("There are " + str(self.n) + "variables");

        self.clauses = []
        self.hashfnc = []
        self.max_Xor = -1 ''' Set this to non-zero value to limit the maximum length of xor constraints
                              If this length is exceeded, xor will be broken up into separate clauses'''
        self.newVar = 0

        while True:
            curline = ifstream.readline()
            if not curline:
                break
            self.clauses.append(curline.strip())
        




def median(self, w):
    srt = sorted(w)
    print (srt)
    self.leng = len(srt)
    if not self.leng % 2:
        return int((srt[ self.leng // 2 ] + srt[ self.leng // 2 - 1]) // 2.0 )
    return int(srt[ self.leng // 2 ] )








def hashfnc_generate(self,m,f)
    self.hashfnc = []
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
                        self.hashfnc.append(temp)
                self.hashfnc.append(newfnc)

    print("Generated " + str(m) + "XOR constraints")
    if self.max_Xor > 0:
        print("Max Xor length is " + str(self.max_Xor) + ". Added " + str(self.newVar)+ "new variables!")
        
