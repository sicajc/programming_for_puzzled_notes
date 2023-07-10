# Sliding Window algorithm
- Concept is imagine you have a window sliding through a fixed sized array, and you are trying to find a certain pattern within this array.
- That is asking if the window I have is the best thing I can do for my objective or not?
- Note the problem genre in puzzle 1 and puzzle 2 are both a type of sliding window problem.
## Naive way
- Simply, for each indices, recalculate the sliding window from that position, which cost $O(n^2)$
- If using the sliding window technique, i.e. adding in stuff and removing out stuff from the window, we can reduce the complexity to $O(n)$

## Simplest problem, the maximum sum of continuous subarray of size K
- This is the simplest problem you can imagine, try to find the starting and ending position of the maximum sum for this size K subarray within a fixed size array.

# Types of sliding window algorithm
## Fixed length size sliding window
- Find the maximum sum of a given subarray.

## Dynamic size sliding window
- Image the window size is varying during sliding through the fixed size array.
- The window gets shrunk or expanded along the way of calculation.
### Example
- Trying to the the smallest sum within an array i.e. greater than or equal to a certain integer value N.

## Dynamic size sliding window with auxiliary data structure
- Usually worked together with hashtable or other data structure
### Example
- Longest length substring with K distinct characters.

# Pattern Recognition of sliding window problem
- Interval items where things are iterated over sequentially.
- Continguos sequence of element, strings, arrays and linked list etc...
- Usually trying to find the minimum of something or the maximum of something, the longest or shortest of something within a fixed size array.
- Running average or moving average.
- Eeverything are grouped sequentially, longest, smallest , contained, the max or min sub structure within an array or buffers etc....