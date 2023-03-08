#! /usr/bin/env python

#Creates Histogram for dice rolls given an input file.

#colloborated w/ Neema and fixed his code to work for Nexp > 1. 
#talked w/ him to understand what the histogram plotting code was doing. 

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
import MySort as mys

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    #initialize counts
    N1 = 0
    N2 = 0
    N3 = 0
    N4 = 0
    N5 = 0
    N6 = 0
    
    data = [] # will turn 2D array into 1D array
    
    Nmeas = 1 #Will redefine later. 
    Nexp = 0 #will count 1 by 1. Each new line in data file is a new experiment.
    
    #Count total number of dice rolls and each count of each dice roll
    with open(InputFile) as ifile:
        for line in ifile: #Each line is a new experiment. 
            lineVals = line.split() #Each experiment.
            Nmeas = len(lineVals) #Each experiment has Nmeas measurements.
            
            for v in lineVals: #each measurement in one experiment.
               val = float(v) #turns each 1, 2, 3, 4, 5, 6 into an actual value 1.0, 2.0, 3.0, 4.0, 5.0, 6.0
               data.append(val) #each measurement in the 2D array gets fed into a 1D array.
            	
               if val == 1: 
                  N1 += 1
            	   
               if val == 2:
                  N2 += 1
            	   
               if val == 3:
                  N3 += 1
            	   
               if val == 4:
                  N4 += 1
            	   
               if val == 5:
                  N5 += 1
            	   
               if val == 6:
                  N6 += 1

            Nexp += 1 

    #Calculate total amount of measurements throughout all experiments
    Ntot = Nmeas * Nexp
   
    #Print out counts of each dice roll to see if counting correctly
    #print(data) 
    print(f"Count of N1: {N1}") 
    print(f"Count of N2: {N2}") 
    print(f"Count of N3: {N3}") 
    print(f"Count of N4: {N4}") 
    print(f"Count of N5: {N5}") 
    print(f"Count of N6: {N6}") 
    print(f"Total Rolls: {Ntot}") 
    
   
    #Calculate Probability of each dice
    N1prob = N1/Ntot
    N2prob = N2/Ntot
    N3prob = N3/Ntot
    N4prob = N4/Ntot
    N5prob = N5/Ntot
    N6prob = N6/Ntot
    Ntotprob = N1prob + N2prob + N3prob + N4prob + N5prob + N6prob
    
    print(f"Probability of N1: {N1prob}") 
    print(f"Probability of N2: {N2prob}") 
    print(f"Probability of N3: {N3prob}")
    print(f"Probability of N4: {N4prob}")
    print(f"Probability of N5: {N5prob}")
    print(f"Probability of N6: {N6prob}")
    print(f"Total Probability: {Ntotprob}") 
    
#Create histogram of counts
    data = np.asarray(data)
    n, bins, patches = plt.hist(data, 16, edgecolor = 'black', linewidth = 3, density = False, facecolor = 'orange', alpha=0.75)

    #turn density off to get total rolls
    
# plot formating options
    plt.xlabel('Value of Simulated Die Roll', fontsize = 15)
    plt.ylabel('Number of Rolls', fontsize = 15)
    plt.title('Randomly Rolled Dice', fontsize = 20)
    plt.grid(True)
    plt.show()


#Normalized Histogram. Probability of each dice roll
    faces = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    probdata = [N1prob, N2prob, N3prob, N4prob, N5prob, N6prob]
    
    plt.bar(faces, probdata, width = 0.4, facecolor = 'orange', edgecolor = 'black')
    plt.xlabel('Value of Simulated Die Roll', fontsize = 15)
    plt.ylabel('Probability of Roll', fontsize = 15)
    plt.title('Probability of Randomly Rolled Dice', fontsize = 20)
    plt.grid(True)
    plt.show()   
