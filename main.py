__author__ = 'uddipaan'


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
    ceiling = math.ceil
    delta = 1 - min_conf
    Q = (((ln(1/delta))/alpha)*ln(n))
    T = ceiling(Q)
    
    w = [ for x in range(T)]
    
    i=0
    while (i <= n) :
        for t in range(1,T):
            
            #hashing to be done
            #find S(h)= size of x for which h(x)=0, hash is 0

            if sh > = 1:           
                w[t] = 1
            else
                w[t] = 0

        med = median(w)
        if med < 1:
            break
        i=i+1
    result = math.pow(2,i-1)
