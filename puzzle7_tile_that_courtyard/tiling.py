#Programming for the Puzzled -- Srini Devadas
#Tile that Courtyard, Please
#Given n in a 2^n x 2^n checkyard with a missing square at position (r, c),
#find tiling of yard with trominoes (L-shaped dominoes).
#This version works directly on the given grid, and does NOT make copies
#of the grid for recursive calls.

EMPTYPIECE = -1

#This procedure is the main engine of recursive algorithm
#nextPiece is the number of next available tromino piece
#The origin coordinates of the yard are given by originR and originC
def recursiveTile(yard, size, originR, originC, rMiss, cMiss, nextPiece):
    # rMiss and cMiss is the position for our statue.
    # Note the size of the problem gets smaller and smaller each time after recursive call.
    #quadrant of missing square: 0 (upper left), 1 (upper right),
    #                            2 (lower left), 3 (lower right)
    quadMiss = 2*(rMiss >= size//2) + (cMiss >= size//2)

    #Base case of 2x2 yard, First determine the base case
    if size == 2:
        # The possible (r,c) row and column position for piece.
        piecePos = [(0,0), (0,1), (1,0), (1,1)]
        # quadMiss is the quadrant of the statue.
        piecePos.pop(quadMiss)
        for (r, c) in piecePos:
            yard[originR + r][originC + c] = nextPiece
        nextPiece = nextPiece + 1
        return nextPiece



    #recurse on each quadrant

    for quad in range(4):
        #Each quadrant has a different origin
        #Quadrant 0 has origin (0, 0), Quadrant 1 has origin (0, size//2)
        #Quadrant 2 has origin (size//2, 0), Quadrant 3 has origin (size//2, size//2)
        # shiftR and shiftC are used to help determines the origin of the quadrant
        shiftR = size//2 * (quad >= 2) # Shift row
        shiftC = size//2 * (quad % 2 == 1) # Shift column
        if quad == quadMiss: # The quad of the missing tile.
            #Pass the new origin for the subproblem
            nextPiece = recursiveTile(yard, size//2, originR + shiftR,\
                originC + shiftC, rMiss - shiftR, cMiss - shiftC, nextPiece)

        else:
            #The missing square is different for each of the other 3 quadrants
            newrMiss = (size//2 - 1) * (quad < 2)
            newcMiss = (size//2 - 1) * (quad % 2 == 0)
            nextPiece = recursiveTile(yard, size//2, originR + shiftR,\
                            originC + shiftC, newrMiss, newcMiss, nextPiece)

    # After solving the subproblems, place the center L-shaped trominoes
    #placing the center tromino, an advanced usage of python
    centerPos = [(r + size//2 - 1, c + size//2 - 1)
                 for (r,c) in [(0,0), (0,1), (1,0), (1,1)]]
    # pop the index location for center position
    centerPos.pop(quadMiss)
    for (r,c) in centerPos: # assign tile to 3 center squares
        yard[originR + r][originC + c] = nextPiece

    # This integer used to store which number of pieces it used, this next piece
    # info is propogate through each recursive calls
    nextPiece = nextPiece + 1


    return nextPiece

#This procedure is a wrapper for recursiveTile that does all the work
def tileMissingYard(n, rMiss, cMiss):
    #Initialize yard, this is the only memory that will be modified!
    yard = [[EMPTYPIECE for i in range(2**n)] for j in range(2**n)]

    recursiveTile(yard, 2**n, 0, 0, rMiss, cMiss, 0)
    return yard

#This procedure prints a given tiled yard using letters for tiles
def printYard(yard):
    for i in range(len(yard)):
        row = ''
        for j in range(len(yard[0])):
            if yard[i][j] != EMPTYPIECE:
                row += chr((yard[i][j] % 26) + ord('A'))
            else:
                row += ' '
        print (row)

print("--------------First yard -------------")
# tiledYard = tileMissingYard(3, 4, 6)
# print(tiledYard)

printYard(tileMissingYard(3, 4, 6))

print("--------------Second yard -------------")
printYard(tileMissingYard(4, 5, 7))