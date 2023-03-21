#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
import Random as rng

# import our Sorting class from MySort.py file
sys.path.append(".")
import MySort as mys

# main function for our Dice Roll Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -input0 [filename]  name of file for H0 data")
        print ("   -input1 [filename]  name of file for H1 data")
        print ("   -p1 [number]     probability of rolling a 1 for H1")
        print ("   -p2 [number]     probability of rolling a 2 for H1")
        print ("   -p3 [number]     probability of rollling a 3 for H1")
        print ("   -p4 [number]     probability of rollling a 4 for H1")
        print ("   -p5 [number]     probability of rollling a 5 for H1")
        print
        sys.exit(1)
        
    #Initialize Probabilities for Null Hypothesis H0, Fair Die
    p1_0 = 1/6
    p2_0 = 1/6
    p3_0 = 1/6
    p4_0 = 1/6
    p5_0 = 1/6
    #only need to specify N-1 faces
    
    #Initialize Probabilities for Alternative Hypothesis H1, Weighted Die
    p1 = 0.3
    p2 = 0.1
    p3 = 0.2
    p4 = 0.1
    p5 = 0.1
    #only need to specify N-1 faces
    #can adjust H1 w/ system terminal inputs
    
    #User needs to provide files that has sampled data from each Hypothesis.
    haveH0 = False
    haveH1 = False

    #System Inputs
    if '-p1' in sys.argv:
        p = sys.argv.index('-p1')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            p1 = ptemp

    if '-p2' in sys.argv:
        p = sys.argv.index('-p2')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            p2 = ptemp

    if '-p3' in sys.argv:
        p = sys.argv.index('-p3')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            p3 = ptemp

    if '-p4' in sys.argv:
        p = sys.argv.index('-p4')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            p4 = ptemp

    if '-p5' in sys.argv:
        p = sys.argv.index('-p5')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            p5 = ptemp   
            
    if '-input0' in sys.argv:
        p = sys.argv.index('-input0')
        InputFile0 = sys.argv[p+1]
        haveH0 = True
        
    if '-input1' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile1 = sys.argv[p+1]
        haveH1 = True
          
    #Analyze Null Hypothesis H0
    data_0 = [] # will turn 2D array into 1D array
    LLR_0 = [] #Log Likelyhood Ratio for each experiment
    
    Nmeas_0 = 1 #Will redefine later. 
    Nexp_0 = 0 #will count 1 by 1. Each new line in data file is a new experiment.
    
    #Calculate Log Likelyhood ratio for each experiment.
    with open(InputFile0) as ifile:
        for line in ifile: #Each line is a new experiment. 
            lineVals = line.split() #All measurements for an experiment.
            Nmeas_0 = len(lineVals) #Each experiment has Nmeas measurements (constant).
            
            #Want to count the number of 1s, 2s, ..., for each experiment
            N1_0 = 0
            N2_0 = 0
            N3_0 = 0
            N4_0 = 0
            N5_0 = 0
            N6_0 = 0          
            
            for v in lineVals: #each measurement in one experiment.
               val = float(v) #turns each 1, 2, 3, 4, 5, 6 into an actual value 1.0, 2.0, 3.0, 4.0, 5.0, 6.0
               data_0.append(val) #each measurement in the 2D array gets fed into a 1D array.
            	
               if val == 1: 
                  N1_0 += 1
            	   
               if val == 2:
                  N2_0 += 1
            	   
               if val == 3:
                  N3_0 += 1
            	   
               if val == 4:
                  N4_0 += 1
            	   
               if val == 5:
                  N5_0 += 1
            	   
               if val == 6:
                  N6_0 += 1

            Nexp_0 += 1
            LLR = Nmeas_0 * np.log(p1_0) - N1_0 * np.log(p1) - N2_0 * np.log(p2) - N3_0 * np.log(p3) - N4_0 * np.log(p4) - N5_0 * np.log(p5) - N6_0 * np.log(1 - (p1 + p2 + p3 + p4 + p5))
            LLR_0.append(LLR)
   
    #Print out results to see if correct
    #print(data_0) 
    #print(LLR_0)
    #print(f"Number of experiments for Null  Hypothesis: {Nexp_0}")
    
    #sort the LLR and find the critical LLR where 5% of LLRs are below it since CL = 95%
    Sorter = mys.MySort()
    LLR_0 = Sorter.DefaultSort(LLR_0) #sort all LLR in ascending order. 
    #print(f"Sorted list of LLR under Null Hypothesis: {LLR_0}")
    
    alpha = 0.05
    LLR_alpha = LLR_0[math.ceil(Nexp_0 * alpha)]
    print(f"Alpha value: {alpha}")
    print(f"The critical LLR_Alpha is: {LLR_alpha}")
    
    #Analyze Alternative Hypothesis H1
    data_1 = [] # will turn 2D array into 1D array
    LLR_1 = [] #Log Likelyhood Ratio for each experiment
    
    Nmeas_1 = 1 #Will redefine later. 
    Nexp_1 = 0 #will count 1 by 1. Each new line in data file is a new experiment.
    
    #Calculate Log Likelyhood ratio for each experiment.
    with open(InputFile1) as ifile:
        for line in ifile: #Each line is a new experiment. 
            lineVals = line.split() #All measurements for an experiment.
            Nmeas_1 = len(lineVals) #Each experiment has Nmeas measurements (constant).
            
            #Want to count the number of 1s, 2s, ..., for each experiment
            N1_1 = 0
            N2_1 = 0
            N3_1 = 0
            N4_1 = 0
            N5_1 = 0
            N6_1 = 0          
            
            for v in lineVals: #each measurement in one experiment.
               val = float(v) #turns each 1, 2, 3, 4, 5, 6 into an actual value 1.0, 2.0, 3.0, 4.0, 5.0, 6.0
               data_1.append(val) #each measurement in the 2D array gets fed into a 1D array.
            	
               if val == 1: 
                  N1_1 += 1
            	   
               if val == 2:
                  N2_1 += 1
            	   
               if val == 3:
                  N3_1 += 1
            	   
               if val == 4:
                  N4_1 += 1
            	   
               if val == 5:
                  N5_1 += 1
            	   
               if val == 6:
                  N6_1 += 1

            Nexp_1 += 1
            LLR = Nmeas_1 * np.log(p1_0) - N1_1 * np.log(p1) - N2_1 * np.log(p2) - N3_1 * np.log(p3) - N4_1 * np.log(p4) - N5_1 * np.log(p5) - N6_1 * np.log(1 - (p1 + p2 + p3 + p4 + p5))
            LLR_1.append(LLR)
   
    #Print out results to see if correct
    #print(data_1) 
    #print(LLR_1)
    #print(f"Number of experiments for Alternative Hypothesis: {Nexp_1}")
    
    #sort LLR_1 and find Beta 
    
    LLR_1 = Sorter.DefaultSort(LLR_1) #sort all LLR in ascending order. 
    #print(f"Sorted list of LLR_1 under Alternative Hypothesis: {LLR_1}")
    
    for i in range(len(LLR_1)):
    	if LLR_1[i] >= LLR_alpha:
    	    LLR_Beta = LLR_1[i]
    	    LLR_Beta_Position = i
    	    print(f"LLR_Beta: {LLR_Beta}")
    	    print(f"Position of LLR_Beta in LLR_1: {LLR_Beta_Position}")
    	    break
                
    Beta = (len(LLR_1) - LLR_Beta_Position)/100 #Beta = perctent of entries in LLR_1 above LLR_alpha
    print(f"Beta value: {Beta}")
    
    Power = 1 - Beta
    print(f"Power of test is: {Power}")
    
    #Create LLR figure
    title = str(Nmeas_0) +  " tosses / experiment"
    
    plt.figure()
    plt.hist(LLR_0, Nmeas_0 + 1, density = True, facecolor = 'b', alpha = 0.5, label = "assuming $\\mathbb{H}_0$")
    
    if haveH1:
        plt.hist(LLR_1, Nmeas_1 + 1, density = True, facecolor = 'g', alpha = 0.7, label = "assuming $\\mathbb{H}_1$")
        plt.legend()

    plt.xlabel('$\\lambda = \\log({\\cal L}_{\\mathbb{H}_{0}}/{\\cal L}_{\\mathbb{H}_{1}})$')
    plt.ylabel('Probability')
    plt.title(title)
    plt.grid(True)

    plt.show()
