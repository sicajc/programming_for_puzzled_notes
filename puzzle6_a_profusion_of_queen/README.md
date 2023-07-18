# N-Queens using Recursive
- Resolving the N-queens using Recursive.


# Correct Recursion consist of 2 parts
1. Base Case must be included where function returns.
2. Recursion is shrinking problems taking bigger problem and making it smaller. The argument to f shall be smaller.


# Formulating Recursive calls
1. Think about a huge exhaustive search tree is being called upon. Each branch is a possible solution for the problem.
2. Backtracking to the previous solution if the solution does no work.
3. Think about an exploding tree, when trying to trace recursive calls. Think about the tree.


# Pruning Search tree
1. To reduce the time complexity, pruning the serach tree with conditions and heuristics to the problem including symmetry and reflection helps a lot.
2. Also representation of the data structure also aids the easier design of the algoritm.

# Notes
1. When thinking about Recursive algorithm, consider BASE CASE, and the ways of dividing large problems into smaller subproblems.
2. Remember to let the function share the same matrix or data structure they are accessing.
