#This is the shorthasher that is going to be incorporated in the extra.py file (i.e in the main program)


import random


def getBiasedBits(num):
	if random.random() < num :
		return 1
	else :
		return 0

def getUnbiasedBits():
	if random.random() < 0.5 :
		return 1
	else :
		return 0


cls = input('Enter the number of clauses\n')
print '# clauses: ',cls
indie = input('Enter the number of independent set\n')
print '# independent sets: ',indie 
f = input('enter the probability of getting 1\n')
print 'prob(1) = ',f

A = [[[]for x in range(indie)] for x in range(cls)]
b = [[] for x in range(cls)]

# need to do random number generation

for i in range(cls):
	for j in range(indie):
		A[i][j]=getBiasedBits(f)

		#A[i][j]=1

for k in range(cls):
	b[k]=getUnbiasedBits()
	#b[k]=0




print('A is: \n')

print A			#A is giving a matrix of Biased bits based on some prob 'f'(1 or 0)

print('\n\n')
print('b is: \n')

print b			#b is giving us a matrix of unbiased bits(1 or 0)

#work left is: 
	# to merge the matrices A and b
	# to merge this hasher with the original program
