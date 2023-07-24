# Memory serves you well

# Dynamic programming
- The art of reducing computational complexity by using memoization. We try to reduce redundant computation by storing the previously calculated result performed by other recursive calls, then when the same recursive call is processed again, the value can be immediatly lookup.

# Formulation of dynamic programming
1. First formulate a recursive problem, try to break the large problem into sub-problems that looks similiar to the problem of the larger problem.
2. Define the base case, sometimes there might be multiple base cases. For the coin picking cases, 2 base cases exist. Skipping the coin leads to 0 coin for base case, also there might be 1 single coin left.
3. Trees can be drawn out o visualize the potential sub-problem of same size in the tree.
4. Also analysis can be done on the drawn tree, for this case since there are N-subproblems. So the time complexity is linear if using memoization. If we purely used recursive algorithm, leads to an exponential time complexity.


# Implementation tips
1. Generally for dynamic programming, we use dictionary for storing data, since most of the case we have to deal with complicated functional calls with a variety of returned results.