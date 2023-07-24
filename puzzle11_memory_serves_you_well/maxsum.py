#Programming for the Puzzled -- Srini Devadas
#Memory Serves You Well
#Take in a list of coins and find selection that maximizes sum.
#Selection obeys the constraint that adjacent coins are not selected.


#This procedure recursively selects coins satisfying the adjacency constraint
#The maximum value for each subproblem is stored in a dictionary memo

def coins(row, table):
    # The original version of coin selection problem without memoization.
    # Usually this type of algoithm must be first derived and checked, so that you can do optimization.

    #Base case: no coins
    if len(row) == 0:
        # Table is used for tracback so that we can derive which coins are selected along the
        # selection process.
        table[0] = 0
        return 0, table
    #base case: one coin, select it
    elif len(row) == 1:
        table[1] = row[0]
        return row[0], table

    #Recursive calls: pick the coin, skip the next.
    #                 Skip the coin.
    #Take the maximum and store the result
    #Two sub-problem, one with picking the current coin, another one skips the current coin.
    #If you select the current coin row[0], you must pick from coin 2
    pick = coins(row[2:], table)[0] + row[0]
    #Since skipping the current coins allows you to pick for position 1
    skip = coins(row[1:], table)[0]
    result = max(pick, skip)
    table[len(row)] = result

    return result, table


#This procedure traces back the coin selection if it is given
#the input row of coins and the maximum values of each subproblem
#stored in the dictionary choices.
def traceback(row, table):

    #Tracing back the coin selection
    select = []
    i = 0
    # This simply start from the table derived, look for the difference of the sum value between N coins
    # and N-1 coins. From the original row, imply which coin is taken then add it into the selected list
    while i < len(row):
        # Two cases, 1 you selected the coin, another one you didnt select the coin.
        if (table[len(row)-i] == row[i]) or \
           (table[len(row)-i] == table[len(row)-i-2] + row[i]):# Must prevent negtive indice
            select.append(row[i])
            #If i was selected i + 1 cannot be!
            i += 2
        else:
            i += 1

    print ('Input row = ', row)
    print ('Table = ', table)
    print ('Selected coins are', select, 'and sum up to', table[len(row)])




#Recursive memoization
def coinsMemoize(row, memo):

    # Creating a memo map to prevent yourself from solving the same problem again.
    if len(row) == 0:
        # No more coins.
        memo[0] = 0
        return (0, memo)
    elif len(row) == 1:
        # 1 coin selected
        memo[1] = row[0]
        return (row[0], memo)

    if len(row) in memo:
        #In this case the subproblem was already solved
        return (memo[len(row)], memo)
    else:
        #Subproblem was not solved, need to solve it
        pick = coinsMemoize(row[2:], memo)[0] + row[0]
        skip = coinsMemoize(row[1:], memo)[0]
        result = max(pick, skip)
        memo[len(row)] = result

        return (result, memo)

row = [14, 3, 27, 4, 5, 15, 1]
result, memo = coins(row, {})
traceback(row, memo)
result, memo = coinsMemoize(row, {})
traceback(row, memo)


lrow = [3, 15, 17, 23, 11, 3, 4, 5, 17, 23, 34, 17, 18, 14, 12, 15]
result, memo = coins(lrow, {})
traceback(lrow, memo)
result, memo = coinsMemoize(lrow, {})
traceback(lrow, memo)
