# The 8 queens problem
- Find a valid solution for the 8 queens problem, where each queen on the 8x8 chessboard, cannot attack each other.

# Naive way
1. Define a 2D grid.
2. Place the queen column by column onto the board.
3. check if no conflict. Conflict means, queens should not attack each other in terms of row,col and diagonal.
4. If no conflict, place the queens onto that certain (row,col) position.
5. If you cannot find a solution, restore the damage(Backtracking). By placing the position of the previous queen, invalidate it to 0.

## checkNoConflict
- Note for every new queen, first check if there exists conflict or not, if there's no conflict, place the queen onto the row of that certain column.
- We only have to check the position we want to place, to ensure that we get the correct position for placing the next queen.

# Better approach
1. Insight, each column has only 1 queen, thus we actually do not need to represent queen's position using a 2D array. We can actually using 1D array storing the row indices of the queen.
2. The checkNoConflict method needs to be modified to accomodate this new data structure.
3. For checking of diagonals, think about the square distance between two queens. We can take the absolute value of the difference, and see the the difference of two queens in terms of x-coordinate and y-coordinate is the same. If they are the same, they are on the same diagonal.
4. Notice there are symmetries exists within this problem, i.e. we do not need to exhaustively check all possible positions.
5. By applying reflection and rotation, we can greatly reduce the numbers of computations needed for this 8-queens problem.

# Implementation details
1. Subfunction noConflict is used to check whether the queen placed violates the rule or not, in CS large problem is given name and different functions to further simplify the problem.
2. Different representation in data structures means different implementation details, correct representation in data structure however, can save more memory, in this case we use 1-D memory representation instead of 2-D memory representation for the location of the queen.