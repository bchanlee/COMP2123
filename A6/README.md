# Assignment 6 - Alien Invasion

## About the code

### Invasion.py

```
is_sorted(A: list) -> bool
```
    Arguments:

        A: A list of integers

    Returns:

        boolean (True, False or None if A is None)

Returns whether the integers stored in A are sorted in increasing order.

```
count_markers(A: list, c: int) -> int
```

* Arguments
    * A: Genetic Markers (a sorted list of integers)
    * c: an integer threshold.

* Returns:
    * integer : The number of markers that satisfy the condition.
        * Note: when A is None, then return None

Returns the number of indices i such that

∣A[i]−i∣≤c

Where i is the index of the element in array A.

Time Complexity: O(log n).

```
break_control(A: list, c: int) -> int
```

Arguments

* A: Genetic Markers (a sorted list of integers)
* c: an integer threshold

Returns:

* Integer: A random index of a number that satisfies the condition.
    * Note: when A is None, then return None
    * If there is no index that can be returned, then return None.

Returns a random index i that satisfies:

∣A[i]−i∣≤c

Time Complexity: O(log n).
