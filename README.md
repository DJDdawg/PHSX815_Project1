# PHSX815_Project1

**Project Idea**

The goal of this project is to simulate rolling a dice many times to see if someone is using a weighted dice.  

 
**Null Hypothesis $H_{0}$**

The dice is fairly weighted: p1 = p2 = p3 = p4 = p5 = p6 = 1/6.

**Alternative Hypothesis $H_{1}$**

The dice is weighted. 

$p1 = 0.3$

$p2 = 0.1$

$p3 = 0.3$

$p4 = 0.1$

$p5 = 0.1$

and $p6 = 1 - (p1 + p2 + p3 + p4 + p5) = 0.1$ from normalization.

**Rolling the Die**

Dice rolls can be simulated with **DiceRoll.py**.

Hypothesis 0 was run in the following way:

> $ python3 DiceRoll.py -Nroll 100 -Nexp 10 -output Dice1.txt

Where '-Nroll xxx' is the number of dice rolls per experiment and 'Nexp xxx' is the number of experiments conducted.

Hypothesis 1 was run by specifying the weighting of each face of the die:

$ python3 DiceRoll.py -p1 0.3 -p20.1 -p3 0.2 -p4 0.1 -p5 0.1  -Nroll 100 -Nexp 10 -output Dice2.txt

The output for both Hypothesis can be seen in **Dice1.txt** and **Dice2.txt**

Make sure that $\Sum_{1}^{6} = 1$ so that you have a valid categorical distribution.

**Plotting Histograms**

**DistHist.py** will plot two histograms for each hypothesis as well as tell you the counts and probabilities of each face on the die.

For the Null Hypothesis it is run with >$ python3 DiceHist.py Dice1.txt and produced the graphs **DiceCount1.png** and **DiceProb1.png** and the following outputs:

>Count of N1: 156

>Count of N2: 181
>
>Count of N3: 172
>
>Count of N4: 160
>
>Count of N5: 156
>
>Count of N6: 175
>
>Total Rolls: 1000
>
>Probability of N1: 0.156
>
>Probability of N2: 0.181
>
>Probability of N3: 0.172
>
>Probability of N4: 0.16
>
>Probability of N5: 0.156
>
>Probability of N6: 0.175
>
>Total Probability: 1.0


![DiceCount1.png](https://github.com/DJDdawg/PHSX815_Week6/blob/main/MonteCarloError.png)


![DiceProb1.png](https://github.com/DJDdawg/PHSX815_Week6/blob/main/MonteCarloError.png)


![DiceCount2.png](https://github.com/DJDdawg/PHSX815_Week6/blob/main/MonteCarloError.png)


![DiceProb2.png](https://github.com/DJDdawg/PHSX815_Week6/blob/main/MonteCarloError.png)

, the first one is a count 
A 6-sided die will be thrown simultaensouly, and their outcome will be recorded.

Initially, this will be done with each side of the die being equally likely (1/6 chance).

Then, this will be repeated with "weighted dice" where one side of a dice is more likely to appear than others. 

The distributions between the various combinations will then be graphed.
 
**How to implement sampling**

Sample a random number from a uniform distribution between 0 and 1.

Assign intervals in this range to correspond to a "face" on the die. 

For the even probability case (as in a normal game): (0, 1/6) = '1', (1/6, 2/6) = '2', and so on. 
 
In the case of a weighted die, the intervals will be adjusted to represent the probability that each face is likely to be landed on.
  
The dice throws will then be stored in a text file and the distribution will be graphed with a histogram. 


**Analysis**

Each dice roll in a single experiment is given by a categorical distribution. 

Rolling the dice multiple times in one experiment will lead to a multinomial distribution.

Make sure to count each dice roll Ntot and how often each face comes up: N1, N2, N3, N4, N5.

Note that N6 = Ntot - (N1 + N2 + N3 + N4 + N5).

We will calculate the Likelyhood Ratio LR = P(N1, N2, ... | Ho)/P(N1, N2, ... | H1) for each experiment done. 

Then calculate Log Likelyhood Ratio by taking log(LR). 

This will be repeated for many experiments. 

Sore the LLR in ascending order.

Select confidence level. Alpha = (1 - confidence level) / 100

Select LLR entry that corresponds to this Alpha value. For a 95% confidence interval this would mean that for the chosen LLR, 95% of LLR values are beneath the chosen value.

Graph LLR vs hypothesis. 

Now when someone rolls dice on us we will be able to determine if they are cheating us or not. Vengeance to the gambling casinos.
