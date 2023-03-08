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

    #create function that rolls a dice
    def Categorical(self, p1, p2, p3, p4, p5):
      R = self.rand(); #samples a random number R from a uniform distribution between 0 and 1. 
    	
      if R < p1:
        return 1
      if R < p1 + p2: 
        return 2
      if R < p1 + p2 + p3:
        return 3
      if R < p1 + p2 + p3 + p4:
        return 4
      if R < p1 + p2 + p3 + p4 + p5:
        return 5
      else:
        return 6
 
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

$ python3 DiceRoll.py -p1 0.3 -p2 0.1 -p3 0.2 -p4 0.1 -p5 0.1  -Nroll 100 -Nexp 10 -output Dice2.txt

The output for both Hypothesis can be seen in **Dice1.txt** and **Dice2.txt**

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


 
**Log Likelyhood Ratio and Comparing Hypothesis**

Each individual dice roll is given by a categorical distribution. 

Rolling the dice multiple times in one experiment will lead to a multinomial distribution: $P(\vec{N}|\vec{p}) = \frac{N_{tot}!}{N_{1}!...N_{k}!} p_{1}^{N_{1}} ... p_{k}^{N_{k}}$,

where $\vec{N}$ is a vector, {$N_{1}, N_{2}, ..., N_{k}$}, that specifies the counts of how many times each face is rolled. 

Note that $\vec{p}$ is unique to each hypothesis. 

The likelyhood ratio (LR) is how to compare the strength of two hypothesis: $LR = \frac{P(x|H_{0})}{P(x|H_{1})}$.

Where "x" is the data obtained, namely $\vec{N}$ under a Hypothesis determined by $\vec{p}$

Plugging in the multinomial distribution for the numerator and denominator yields, $LR = \frac{p_{01}^{N_{1}} p_{02}^{N_{2}} p_{03}^{N_{3}} p_{04}^{N_{4}} p_{05}^{N_{5}} p_{06}^{N_{6}}}{p_{1}^{N_{1}} p_{2}^{N_{2}} p_{3}^{N_{3}} p_{4}^{N_{4}} p_{5}^{N_{5}} p_{6}^{N_{6}}} = \frac{p_{0}^{N_{1} + N_{2} + N_{3} + N_{4} + N_{5} + N_{6}}}{p_{1}^{N_{1}} p_{2}^{N_{2}} p_{3}^{N_{3}} p_{4}^{N_{4}} p_{5}^{N_{5}} p_{6}^{N_{6}}} = \frac{p_{0}^{N_{tot}}}{p_{1}^{N_{1}} p_{2}^{N_{2}} p_{3}^{N_{3}} p_{4}^{N_{4}} p_{5}^{N_{5}} p_{6}^{N_{6}}}$,

since the normalization factors cancels, and all of the probabilities in the Null hypothesis are equal.

A more useful metrix that can turn all of this multipliation into addition is the Log Likelyhood Ratio (LLR), which is defined as the name sounds:

$LLR = \log (LR) = \log (\frac{p_{0}^{N_{tot}}}{p_{1}^{N_{1}} p_{2}^{N_{2}} p_{3}^{N_{3}} p_{4}^{N_{4}} p_{5}^{N_{5}} p_{6}^{N_{6}}}) = \log (p_{0}^{N_{tot}}) - \log (p_{1}^{N_{1}} p_{2}^{N_{2}} p_{3}^{N_{3}} p_{4}^{N_{4}} p_{5}^{N_{5}} p_{6}^{N_{6}}) = N_{tot} \log (p_{0}) - \sum_{i=1}^{6} N_{i}\log (p_{i})$.

**Confidence Levels and Power of Test**

The above LLR is calculated for each experiment and added to an array { $LLR_{1}, LLR_{2}, ..., LLL_{N_{exp}}$ } and is then sorted in ascending order.

Now we select our confidence level for the experiment:

Picking a confidence level is done by choosing a value $\alpha = \frac{1 - CL}{100}$. For this simulation we will choose $\alpha = 0.05$ so that our Confidence Level is 95%. 

We know comb through our LLR array and choose the entry, $LLR_{\alpha}$, that corresponds to our confidence level. For a 95% confidence interval this would mean that 95% of LLR values are beneath the value $LLR_{\alpha}$.

We then head on over to our counterpart Log likelyhood ratio assumning $H_{1}$ instead of $H_{0}$. Namely, $LLR = \frac{P(x|H_{1})}{P(x|H_{0})} = \sum_{i=1}^{6} N_{i}\log (p_{i}) - N_{tot} \log (p_{0})$.

Graph LLR vs hypothesis. 

Now when someone rolls dice on us we will be able to determine if they are cheating us or not. Vengeance to the gambling casinos.
