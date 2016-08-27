__author__ = 'uddipaan'

#from SparseCount import *
#from sat import sat
from extra import median 

#Usage
#parameter 1: Name of the problem file
#parameter 2: Alpha value

if __name__ == '__main__':
    if len(sys.argv)<1:
        print("Error. Quiting!!");
        exit(1);

    prb_nme = sys.argv[1]
    alpha = sys.argv[2]

    
    
    ln = math.log
    sqrt = math.sqrt
    ceil = math.ceil
    delta = 1 - min_conf
    Q = (((ln(1/delta))/alpha)*ln(n))
    T = ceil(Q)
    
    w = [[0 for x in range(n)] for y in range(T)]
    
    i=0
    while (i <= n) :
        for t in range(1,T):
            
            #hashing to be done
            #find S(h)= size of x for which h(x)=0, hash is 0

            #the indicator function is applied below
            if sh > = 1:           
                w[i][t] = 1
            else
                w[i][t] = 0

        med=median(i, t, w)
        if med < 1:
            break
        i=i+1
    result = math.pow(2,i-1)
