# Disorganized handyman
- Assume x100 nuts and bolts of different size, want the nuts and bolts to be connected correctly in the most efficient way.


# Divide and Conquer
1. Divide and conquer is extremely efficient since it has a time complexity of log_2_n
2. Howeer, sometimes sub-problems might not be solvable, thus what to do?

# QuickSort
## Pivots
1. Choose a random number, take it as a pivot, and the start comparing the pivot which all the remaining elements.
2. Then perform divide and conquer, do the same thing to the elements smaller than the pivot, also to the elements larger than the pivot.
3. To reduce the complexity further, one usually randomized the array before getting sorted. Known as the randomized quickSort.


## In-place quickSort
- The memory requirement of quickSort is much smaller than the memory requirement of mergSort
1. By using 1 additional integer storage, we are now able to perform in-place quickSort.
2. In-place quickSort is the reason why most built-in sort functions nowadays ultilize QuickSort algorithm for the optimal performance.

## Implmentation detail
1. Additional 1 variable storage is used, 1 integer to perform in place storage
2. In python, this kind of printing statement is viable.
```python
    print ('Partition start: bottom =', start - 1, 'top = ', end)
```