# Best time to party
- Find the best interval to arrive to meet the most celebrities.


# Naive approach
1. First check for the schedule of each celebrities.
2. Find out the union of the intervals of the presentation of all the celebrities.
3. From this union, calculate the density of each time instance. The density means the total precedence of celebrities exist in that time instance.
4. Then find the time instance with the largest density.

# Clever Approach
## Concept of Incremental Computation
>> Whenever density changes, it must be celebrities entering or leaving the party.
- There is always an opportunity to reduce the whole algorihm into incremental computation.

1. Sort the celebrities in an increasing order in terms of starting time instance.
2. For all the intervals within this new celebrity schedule.
    1. Whenever a celebrity enters the party, increase the density by 1, if leaving decrement the density by 1, otherwise do nothing.
    2. Whenever a celebrity enters, do the comparison with the max density.


# Note
1. Since starting time and ending time can be treated as different objects, you might as well just seperate them out. And create a new list for iterating them.
2. Sometimes sorting can works wonder on the data you are trying to process.
3. These kind of problem can be viewed as Sliding Window problem.

# Implementation details
1. Additional data structure like tuple can helps you solve problem, this helps convey the information that this is the time starting also the time ending of this particular schedule.
2. Since we only care about start time and end time, i.e. start time +1 end time -1, thus preprocess and break the time into two part, the start and end.
```python
  for c in schedule:
        times.append((c[0], 'start'))
        times.append((c[1], 'end'))
```
