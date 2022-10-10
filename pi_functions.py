#----------------------------------------------------------------------------
#    PROGRAM NAME:  pi_functions.py
#    PURPOSE:       first example with functions
#                   calculate pi with MC inegration
#    CREATED:       Craig Group  2022
#
#    Class09
#    UVA Honor Pledge
#   
#    To run me:  python pi_functions.py N seed
#____________________________________________________________________________

#------------------------------------------------
#                  IMPORTS
#------------------------------------------------
import numpy as np
import sys

#------------------------------------------------
#               GLOBAL CONSTANTS
#------------------------------------------------
YMIN=-1
YMAX=1
XMIN=-1
XMAX=1
SEED=1  #Default seed value


#------------------------------------------------
#               METHODS
#------------------------------------------------

#Pull 2 random number arrays between max and min values
def rand_array(N,myseed):   
    np.random.seed(myseed)
    x=np.random.random(N)*(YMAX-YMIN)-YMAX 
    y=np.random.random(N)*(XMAX-XMIN)-XMAX
    return x,y

def calc_pi(N,seed=SEED):  #Example of providing a default input variable
    print(f"N={N}, seed={seed}\n")
    x,y=rand_array(N,seed)
    #Calculate the number of points inside the circle
    n_in=np.count_nonzero(np.less(np.sqrt(x*x+y*y),1))
    my_pi=(XMAX-XMIN)*(YMAX-YMIN)*n_in/N
    return my_pi
    
#------------------------------------------------
#                   MAIN FUNCTION
#------------------------------------------------
def main():
    print(f"You are executing the main function of {sys.argv[0]}")
    my_pi=calc_pi(10000,1)
    print(my_pi)    

 
#Call the main function only if being run as a script
if __name__ == "__main__":
    main()
