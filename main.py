__author__ = 'uddipaan'



'''REVISIONS !!! '''
# f value needs to be revised
# alpha value is user input






from extra import * 

#Usage
#parameter 1: Name of the problem file
#parameter 2: Alpha value
#parameter 3: Minimum confidence

if __name__ == '__main__':
    if len(sys.argv)<1:
        print("Error. Quiting!!");
        exit(1);

    prb_nme = sys.argv[1]
    alpha = sys.argv[2]
    min_conf = sys.argv[3]

    prb = SAT(prb_nme)

    min_m = 0 #no. of  minimum parity constraints is 0
    if max_m < 0:
        max_m = prb.n #max no. of parity constraints is the no. of variables in the problem


    

    
    ln = math.log
    sqrt = math.sqrt
    ceiling = math.ceil
    delta = 1 - min_conf
    Q = (((ln(1/delta))/alpha)*ln(prb.n))
    T = ceiling(Q)
    
    w = [ for x in range(T)] #here w is initialized to the range of T
    
    i=0
    while (i <= prb.n) :   
        for t in range(1,T):
            
            
            m=i
            f=0.02 #just for now
            hashfnc_generate(m, f)  #hash functions generated
            
            outcome=solver()
            
            #find S(h)= size of x for which h(x)=0, hash is 0

            if sh > = 1:           
                w.append(1)
            else
                w.append(0)

        med = median(w)
        if med < 1:
            break
        i=i+1
    result = math.pow(2,i-1)
