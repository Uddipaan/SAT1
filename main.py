__author__ = 'uddipaan'

import math   #(for python less than or equal to version 2, use this import part)
import sys
import argparse     #argparser is a library
import time


from extra import *

#Usage
#parameter 1: Name of the problem file
#parameter 2: Alpha value
#parameter 3: Minimum confidence

if __name__ == '__main__':
    if len(sys.argv)<1:
        print("Error. Quiting!!");
        exit(1);


    parser = argparse.ArgumentParser() #This is a constructor where ArgumentParser is the class name
    parser.add_argument(dest='prb_nme',help="Name of the problem file")
    parser.add_argument(dest='alpha',help="Alpha value",type=float)
    parser.add_argument(dest='min_conf',help="Minimum Confidence",type=float)
    args, unknown = parser.parse_known_args() #using parse_known_args rather than parse_args enables the use of ArgumentParser in code within the scope of if __name__ == 'main':

   
    prb_nme = args.prb_nme
    alpha = args.alpha
    min_conf = args.min_conf

    prb = SAT(prb_nme)


    start_time = time.time()
    ln = math.log
    sqrt = math.sqrt
    ceiling = math.ceil
    delta = 1 - min_conf
    Q = (((ln(1/delta))/alpha)*ln(prb.n))
    T = int(ceiling(Q))
    
    print "The Value of T= "+str(T)
    
    
    i=0
    while (i <= prb.n) :  
	w=[] 
        for t in range(1,T):
		
                m=i
            	if not os.path.isdir("tmp"):
            		os.mkdir("tmp")
		finalFile= "tmp/SAT_test.cnf"
		prb.addHash(prb_nme, finalFile, m)
		sh = prb.solver(finalFile)
		if sh != 0:
               		if sh == True:           
                    		w.append(1)
                	else:
                    		w.append(0)
            	else:
                	print("No results for i= "+str(i)+" and t= "+str(t))
       	med = median(w)
	if med < 1:
	   	print("Median is less than one")
            	break
    	i=i+1
    
    
    result = math.pow(2,i-1) 
    print("time taken: %s seconds" % (time.time() - start_time))
    print("For a CNF formula with "+str(prb.n)+" variables and "+str(prb.no_of_clauses)+" clauses with given tolerance = "+str(alpha)+" and minimum confidence = "+str(min_conf)+" we have, ")
    print("The result is " + str(math.floor(result)))
    os.system('rm '+finalFile)  
