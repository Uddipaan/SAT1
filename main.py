__author__ = 'uddipaan'

from SparseCount import *
from sat import sat

#Usage
#parameter 1: Name of the problem file

if __name__ == '__main__':
    if len(sys.argv)<1:
        print("Error. Quiting!!");
        exit(1);

    prb_nme = sys.argv[1]
    prb = SAT(prb_name)
    
