# Problem 6: Unsorted Integer Array

"""
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers.
The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

"""

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 0:
        return []
    min_int = ints[0]
    max_int = ints[len(ints) - 1]
    min_max = ()
    for i in ints:
        if i <= min_int:
            min_int = i
        if i >= max_int:
            max_int = i
    min_max = (min_int, max_int)

    return min_max


print("\n----------test cases given in the problem------------")
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print("\n-----------other test cases------------------")
print("\nrange from 123 to 134")
k = [i for i in range(123, 135)]     # does NOT include 135, so max returned would be 134
random.shuffle(k)
print("Pass" if (123, 134) == get_min_max(k) else "Fail")

p = []
#random.shuffle(k)             # since we are pssing empty list, no need to shuffle
print("Pass" if [] == get_min_max(p) else "Fail")

q = [0,0]
print("\n-----------[0,0] should return 0,0")
print("Pass" if (0,0) == get_min_max(q) else "Fail")

# the above test cases should print the following results
"""
----------test cases given in the problem------------
Pass

-----------other test cases------------------

range from 123 to 134
Pass
Pass

-----------[0,0] should return 0,0
Pass

"""