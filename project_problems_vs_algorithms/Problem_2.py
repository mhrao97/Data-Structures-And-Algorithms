# Problem 2: Search in a Rotated Sorted Array
"""
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be
in the order of O(log n).
"""

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """


    # check if array is rotated - if a pivot is found, then array is rotated
    # if a pivot is not found, then array is not rotated
    # on a rotated array, compare the number with the pivot, then search
    # the two sub-arrays around the pivot
    pivot = find_pivot(input_list, 0, len(input_list) - 1)

    if pivot == -1:
        return binary_search(input_list, 0, len(input_list) - 1, number)

    if input_list[pivot] == number:
        return pivot

    if input_list[0] <= number:
        return binary_search(input_list, 0, pivot - 1, number)

    return binary_search(input_list, pivot + 1, len(input_list) - 1, number)


def find_pivot(arr, start_index, end_index):
    if start_index > end_index:
        return -1
    if start_index == end_index:
        return start_index

    mid_index = (start_index + end_index) // 2

    if mid_index < end_index and arr[mid_index] > arr[mid_index + 1]:
        return mid_index

    if mid_index > start_index and arr[mid_index] < arr[mid_index - 1]:
        return (mid_index - 1)

    if arr[start_index] >= arr[mid_index]:
        return find_pivot(arr, start_index, mid_index - 1)

    return find_pivot(arr, mid_index + 1, end_index)


def binary_search(array, start_index, end_index, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
      start_index: initial position to start search
      end_index: last position to end search

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    while start_index <= end_index:
        mid_point = (start_index + end_index) // 2

        mid_item = array[mid_point]

        if target == mid_item:
            return mid_point

        elif target < mid_item:
            end_index = mid_point - 1

        else:
            start_index = mid_item + 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    if len(test_case) != 2:
        print("Please provide both - an array and a target")
        return

    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


print("\n----------test cases given in the problem------------")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

print("\n-------edge cases---------------------")
print("\ncase where a target is searched in an empty array")
test_function([[],0])
print("\ncase where target is not passed in an empty array")
test_function([[],])
print("\ncase where an array is passed but target is missing")
test_function([[6, 7, 8, 1, 2, 3, 4]])

# the above test cases should print the following results
"""
----------test cases given in the problem------------
Pass
Pass
Pass
Pass
Pass

-------edge cases---------------------

case where a target is searched in an empty array
Pass

case where target is not passed in an empty array
Please provide both - an array and a target

case where an array is passed but target is missing
Please provide both - an array and a target

"""