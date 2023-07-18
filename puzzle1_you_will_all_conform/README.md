# You will all conform
- Goal is to code out the minimal line of code s.t. we can flip the caps of a team of baskest ball members standing in line into the same direction, however, we can only flip each person at once.

## Naive PseudoCode
- Do the first pass to  generate the forward intervals and backward intervals.
- Do the second pass to flip the caps, if the intervals you are passing through is backward, flips the cap.
- Code out the boundary condition of the last element.

## Insight
- Notice the boundary condition could be handled by what we called, preprocessing, by adding another distinct element to the end of the list, thus we can prevent the boundary condition checking.
- Since we only want the line to be in a single direction of cap, thus simply sees what the first element is, then flips the caps in terms of that certain direction.
- Doing so we can allow the whole lines to get flipped into the same direction as we go through the line.

## NOTE
- Adding additional boundary can greatly simplify the logic.
- Think about the problem in a high level thought way instead of directly implementing the algorithm in terms of code.
- Play with some examples to gain insight about the problem.

## Preprocessing
```python
    caps = caps + ['END']

```