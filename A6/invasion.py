"""
Alien Invasion
--------------
Your job is to help write the required algorithms to perform these tasks and
save the human race, before all hope is lost! Good luck!
The fate of humanity rests on your shoulders...
--------------

This module will contain all functions that you must implement. It will serve
as the main file to be created during testing.

Usage:
    - Contains functions that will be implemented to stop the Alien Invasion!
"""

import random
import math


class AlienInvasion:
    """
    Alien Invasion Class
    Contains three functions to be implemented:

    1. `is_sorted(A)` - returns whether the array is sorted.
    2. `count_markers(A, c)` - returns the number of indices `i` such that
                                | A[i] - i | <= c.
    3. `break_control(A, c)` - returns a "random" index that satisfies
                               |A[i] - i | <= c.
    """

    @staticmethod
    def is_sorted(A: list) -> bool:
        """
        Checks whether the given list of genetic code is sorted in
        increasing order.

        If the array (A) is None, return None.
        :param A: A list of indices.
        :return: True if sorted, else False.
        """
        if A is None:
            return None
        n = len(A)
        if n == 0 or n == 1:
            return True
        for i in range(0, n-1):
            if A[i] > A[i+1]:
                return False
        return True

    def optimal_index(self, A: list) -> int:
        n = len(A)
        low = 0
        high = n - 1
        while low <= high:
            mid = (high + low) // 2
            bool = True
            e = abs(A[mid] - mid)
            if mid == 0 or mid == n - 1:
                return -1
            e_before = abs(A[mid-1] - mid + 1)
            if e >= e_before:
                bool = False
                high = mid - 1
                continue
            e_after = abs(A[mid+1] - mid - 1)
            if e > e_after:
                bool = False
                low = mid + 1
                continue
            if bool == True:
                return mid
        return -1


    def count_markers(self, A: list, c: int) -> int:
        """
        :param A: A **SORTED** array of integers in increasing order.
        :param c: The integer threshold
        :return: The number of elements that satisfy the condition.
        """
        if A is None:
            return None
        if c is None:
            return None
        if c < 0:
            return None
        n = len(A)
        if n == 0:
            return 0
        # base case?
        if n == 1:
            if abs(A[0]) <= c:
                return 1
            return 0
        # divide - O(logn) = T(n/2) + O(1)
        # binary search
        # """
        low = 0
        high = n - 1
        res = 0
        first = abs(A[low])
        last = abs(A[high]-high)
        if first <= last:
            while low <= high:
                mid = (high + low) // 2
                e = A[mid] - mid
                if abs(e) <= c:
                    res = mid+1
                    low = mid + 1
                else:
                    high = mid - 1
        else:
            mid = (high + low) // 2
            for i in range(mid, len(A)):
                if abs(A[i] - i) <= c:
                    res += 1
        return res
        """
        res = 0
        low  = 0
        high = n -1
        val = self.optimal_index(A)
        # either ascending or descending
        if val == -1:
            first = abs(A[low])
            last = abs(A[high]-high)
            if first <= last:
                val = -1
            else:
                val = n # n and n - 1 failed
        ascending = 0
        descending = 0
        # all descending
        low = 0
        high = val
        while low <= high:
            mid = (high + low) // 2
            e = A[mid] - mid
            if abs(e) <= c:
                descending = val - mid
                high = mid - 1
            else:
                low = mid + 1
        # all ascending
        low = val + 1
        high = n - 1
        while low <= high:
            mid = (high + low) // 2
            e = A[mid] - mid
            if abs(e) <= c:
                ascending = mid - val
                low = mid + 1
            else:
                high = mid - 1
        res = ascending + descending
        return res
        # """


    def break_control(self, A: list, c: int) -> int:
        """
        Returns a **random** index such that A[i] satisfies:
            | A[i] - i | <= c

        If there are no numbers/indices that satisfy the conditions, or if
        the array is None, return `None`.

        :param A: A **SORTED** list of integers in increasing order.
        :param c: The integer threshold.
        :return: The **INDEX** of an element that satisfies the condition.
        """
        if A is None:
            return None
        if c is None:
            return None
        if c < 0:
            return None
        n = len(A)
        if n == 0:
            return None
        # base case?
        if n == 1:
            if abs(A[0]) <= c:
                return 0
            return None

        arr = []
        low  = 0
        high = n -1

        val = self.optimal_index(A)

        # either ascending or descending
        if val == -1:
            first = abs(A[low])
            last = abs(A[high]-high)
            if first <= last:
                val = -1
            else:
                val = n-1 # n-1 here not n? n makes it fail randomness check

        # all descending
        low = 0
        high = val
        while low <= high:
            mid = (high + low) // 2
            e = A[mid] - mid
            if abs(e) <= c:
                arr.append(mid)
                high = mid - 1
            else:
                low = mid + 1

        # all ascending
        low = val + 1
        high = n - 1
        while low <= high:
            mid = (high + low) // 2
            e = A[mid] - mid
            if abs(e) <= c:
                arr.append(mid)
                low = mid + 1
            else:
                high = mid - 1

        if len(arr) > 0:
            t = random.randint(0, len(arr)-1)
            return arr[t]
        return None

        """
        low = 0
        high = n - 1
        res = 0
        first = abs(A[low])
        last = abs(A[high]-high)

        # Naive
        arr = []
        mid = (high + low) // 2
        if first <= last:
             while low <= high:
                 mid = (high + low) // 2
                 e = A[mid] - mid
                 if abs(e) <= c:
                     arr.append(mid)
                     low = mid + 1
                 else:
                     high = mid - 1
        else:
            for i in range(mid, n):
                if abs(A[i] - i) <= c:
                    arr.append(i)
        if len(arr) > 0:
            t = random.randint(0, len(arr)-1)
            return arr[t]

        for i in range(0, n):
            if abs(A[i] - i) <= c:
                arr.append(i)
        if len(arr) > 0:
            t = random.randint(0, len(arr)-1)
            return arr[t]
        return None
        """
