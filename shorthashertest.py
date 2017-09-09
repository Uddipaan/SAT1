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
print '# of clauses: ',cls
indie = input('Enter the number of independent set\n')
print '# of independent sets: ',indie 
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

print('\n')
print('b is: \n')

print b			#b is giving us a matrix of unbiased bits(1 or 0)


merged_matrix = [[0 for x in range(indie+1)] for y in range(cls)]



for i in range(cls):
	for j in range(indie):
		merged_matrix[i][j]=A[i][j]

for j in range(cls):
	merged_matrix[j][indie]=b[j]

print('\n')

print merged_matrix

#work left is: 
	# to merge this hasher with the original program
