#Programming for the Puzzled -- Srini Devadas
#A Profusion of Queens
#Given the dimension of a square "chess" board, call it N, find a placement
#of N queens such that no two Queens attack each other using recursive search

#This procedure initializes the board to be empty, calls the recursive N-queens
#procedure and prints the returned solution
def nQueens(size):
    # -1 representation used to indicate the board is empty.
    board = [-1] * size
    rQueens(board, 0, size)
    print (board)

#This procedure checks that the most recently placed queen on column current
#does not conflict with queens in columns to the left.
def noConflicts(board, current):
    for i in range(current):
        # Check for same rows
        if (board[i] == board[current]):
            return False
        # Check for diagonals
        if (current - i == abs(board[current] - board[i])):
            return False
    return True


#This procedure places a queens on the board on a given column so it does
#not conflict with the existing queens, and then calls itself recursively
#to place subsequent queens till the requisite number of queens are placed
def rQueens(board, current, size):
    if (current == size):
        # Base Case
        return True
    else:
        # Exhaustive search for all cases.
        for i in range(size):
            # For all rows of this current column Place the queen onto the board
            board[current] = i
            # Check if this leads to a conflict.
            if (noConflicts(board, current)):
                # If there is no conflict, shrink the board, start placing another queen.
                done = rQueens(board, current + 1, size)
                if (done):
                    return True
        return False

nQueens(20)