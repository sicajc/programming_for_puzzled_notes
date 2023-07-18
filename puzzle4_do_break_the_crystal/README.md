# Break the crystal
- Shanghai tower exists and there is 128 floors. We have d balls, how many drops do we need to find the hardness coefficient, i.e. the number of floors which ball can witstands.

# d = 2, when we have 2 balls
## Binary Search method
- When we have 2 balls, we can first try Binary search, drop the balls from 64 floors. But then we have to try 1~63 if the ball breaks, which is the worst case.

## Intervals
- Divide 128 into 8 intervals where every interval is 16 floors. If we start dropping balls from 16,32,48 etc... Assume if the ball breaks at 128, we only need to test 112~127 floors. How to do Analysis on this to find the number of drops needed to determine the hardness coefficient of the ball.

# How to generalized this observation?
- i.e. given n floors and d balls, how many number of drops do we need to check the hardness of our ball?

# Worst Case Analytic Analysis
- Let n be the number of floors, k be the size of interval.
- k,2k,3k,..... , (n/k-1)k,(n/k)*k, goal is trying to find the best k.
- We can eventually from this analysis standpoint, find out that the floor(squareroot of n) is close to the worst case drop.
- However, Unequal size of interval can be ultilized to improve performance.
# Radix(d-digit , r-ary number Representation)
1. Think about d-digit numbers, counting a multiple of k-ary numbers. Figuring out the best radix r s.t. $r^d > n$. Which is the result of analysis.
2. Thus for number n= 128, uses r = 4, d = 4. i.e. 4 digits under a radix of 4.

# Note
- Learning how to do worst case analysis is important to gain insight toward the algorithm.

# Implementation details
1. Radix is represented using list in python, and modifying list means modifying that r-ary representation.
2. This floorNoBreak is used to store the representation of the r-ary number.
```python
    floorNoBreak = [0] * d
```
