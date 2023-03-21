#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np

# import our Random class from python/Random.py file
sys.path.append(".")
import Random as rng

# main function for our dice roll
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

    # default probability for 6-sided die
    p1 = 1/6
    p2 = 1/6
    p3 = 1/6
    p4 = 1/6
    p5 = 1/6
    #only need to specify N-1 faces

    # default number of dice rolls (per experiment)
    Nroll = 1

    # default number of experiments
    Nexp = 1

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
        
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
                   
    if '-Nroll' in sys.argv:
        p = sys.argv.index('-Nroll')
        Nr = int(sys.argv[p+1])
        if Nr > 0:
            Nroll = Nr
            
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
            
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # class instance of our Random class using seed
    random = rng.Random(seed)

    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                outfile.write(str(random.Categorical(p1, p2, p3, p4, p5))+" ")
            outfile.write(" \n")
        outfile.close()
    else:
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                print(rng.Categorical(self, p1, p2, p3, p4, p5), end=' ')
            print(" ")
   
