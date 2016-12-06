import os


outputFileName = "tmp/test.cnf"
cmd="./cryptominisat5  --verb=0 SAT_test.cnf > "+str(outputFileName)
os.system(cmd)
f= open(outputFileName,'r')
lines = f.readlines()
f.close() 
print("DONE")


res = lines[0]
head = res.split()

print head[1]

if head == 0:
	print("EKU NAI")
else:
	print("EKU ASE")
	if head[1] == 'SATISFIABLE':
        	print("SAT")
        elif head[1] == 'UNSATISFIABLE':
                print("UNSAT")
