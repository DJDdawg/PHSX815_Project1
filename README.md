# PHSX815_Project1

**Project Idea**

The goal of this project is to simulate rolling a dice many times to see if someone is using a weighted dice.  

 
**What the Code will do**

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

Two Hypothesis Exist.

Ho: All probabilities are equal. p1 = p2 = p3 = p4 = p5 = p6.

H1: Weighted dice. 

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

Now when someone rolls dice on us we will be able to determine if they are cheating us or not. Vengeance to the gambling casinos!
