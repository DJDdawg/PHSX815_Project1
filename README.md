# PHSX815_Project1

**Project Idea**

The goal of this project is to simulate rolling a dice many times to see if someone is using a weighted dice.  

**Background Knowledge on Categorical Distributions**

A Categorical Distribution is a generalization of the Bernoulli Distribution to k possible outcomes. In the case of a standard die, $k = 6$.

The Categorical Distribution has the form of a "pick me" function: $P(x | \vec{p}) = p_{1}^{x=1} p_{2}^{x=2} ... p_{k}^{x=k}$, where $\vec{p}$ is a vector of the different probabilities of $k - 1$ outcomes, and the probability of $x = i$ is $p_{i}$: hence you "pick out" the probability of the face that you are interested in rolling. The probability of the $k^{th}$ outcome comes from normalization: $\sum_{i=1}^{k} p_{i} = 1$.

In general, the algorithm for a Categorical Distribution function works as follows:

1. Sample a random number R from a uniform distribution between 0 and 1.

2. Assign intervals in this range to correspond to a probabilities "face" on the die. 

The code that implements the Categorical Distribution for a 6-sided die can be seen in **Random.py**.
 
**Null Hypothesis $H_{0}$**

The dice is fairly weighted: $p_{1} = p_{2} = p_{3} = p_{4} = p_{5} = p_{6} = \frac{1}{6}$

**Alternative Hypothesis $H_{1}$**

The dice is weighted. 

$p_{1} = 0.3$

$p_{2} = 0.1$

$p_{3} = 0.3$

$p_{4} = 0.1$

$p_{5} = 0.1$

and $p_{6} = 1 - (p_{1} + p_{2} + p_{3} + p_{4} + p_{5}) = 0.1$ from normalization.

**Rolling the Die**

Dice rolls can be simulated with **DiceRoll.py**.

Hypothesis 0 was run in the following way:

> $ python3 DiceRoll.py -Nroll 100 -Nexp 10 -output Dice1.txt

Where '-Nroll xxx' is the number of dice rolls per experiment and 'Nexp xxx' is the number of experiments conducted.

Hypothesis 1 was run by specifying the weighting of each face of the die:

$ python3 DiceRoll.py -p1 0.3 -p20.1 -p3 0.2 -p4 0.1 -p5 0.1  -Nroll 100 -Nexp 10 -output Dice2.txt

The output for both Hypothesis can be seen in **Dice1.txt** and **Dice2.txt**

Make sure that $\sum_{1}^{6} p_{i} = 1$ so that you have a valid categorical distribution.

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


![DiceCount1.png](https://github.com/DJDdawg/PHSX815_Project1/blob/main/DiceCount1.png))


![DiceProb1.png](https://github.com/DJDdawg/PHSX815_Project1/blob/main/DiceProb1.png)

Similarly, the rolling for the alternative hypothesis $H_{1}$ was done and produced **DiceCount2.png** and **DiceProb2.png**.

>$ python3 DiceHist.py Dice2.txt
>
>Count of N1: 293
>
>Count of N2: 181
>
>Count of N3: 195
>
>Count of N4: 84
>
>Count of N5: 114
>
>Count of N6: 133
>
>Total Rolls: 1000
>
>Probability of N1: 0.293
>
>Probability of N2: 0.181
>
>Probability of N3: 0.195
>
>Probability of N4: 0.084
>
>Probability of N5: 0.114
>
>Probability of N6: 0.133
>
>Total Probability: 1.0

![DiceCount2.png](https://github.com/DJDdawg/PHSX815_Project1/blob/main/DiceCount2.png)


![DiceProb2.png](https://github.com/DJDdawg/PHSX815_Project1/blob/main/DiceProb2.png)


 
**Log Likely Hood Ratio and Comparing Hypothesis**


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
