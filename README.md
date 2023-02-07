# PHSX815_Project1

Project Idea
  The goal of this project is to simulate a simplified version of the game of Yahtzee!. 
  Yahtzee is a game where you roll 5 die and various combinations give you a different amount of points. Normally, 5 die are used. After 13 rounds, the player with the most points wins.
  This project will only use two die. 
 
What the Code will do
  Two 6-sided die will be thrown simultaensouly, and their outcome will be recorded.
  Initially, this will be done with each side of the die being equally likely (1/6 chance).
  Then, this will be repeated with "weighted dice" where one side of a dice is more likely to appear than others. 
  The distributions between the various combinations will then be graphed.
 
How to implement sampling
  Sample a random number from a uniform distribution between 0 and 1.
  Assign intervals in this range to correspond to a "face" on the die. 
  For the even probability case (as in a normal game): (0, 1/6) = '1', (1/6, 2/6) = '2', and so on. 
  In the case of a weighted die, the intervals will be adjusted to represent the probability that each face is likely to be landed on.
  These pairs of dice throws will then be stored in a text file and then graphed. 
  
  Possible combinations can be represented by a double sum. Sum(i)Sum(j) of (Di, Dj).
    Note that (Di, Dj) = (Dj, Di). This means that (1,2) is the same as (2,1).
    
  All the possible combinations for a two sided die are the following (there are 6^2 possibilities):
    (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), 
    (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), 
    (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), 
    (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), 
    (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), 
    (6,1), (6,2), (6,3), (6,4), (6,5), (6,6)
