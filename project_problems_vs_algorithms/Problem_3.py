# Problem 3: Rearrange Array Digits
"""
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum.
Return these two numbers. You can assume that all array elements are in the range [0, 9].
The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any
sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as
these when there are more than one possible answers, return any one.
"""

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return 0, 0

    sorted_input = merge_sort(input_list)
    even = 0
    odd = 0

    for i in range(len(sorted_input)):
        if i % 2 == 0:
            even = even * 10 + sorted_input[i]
        else:
            odd = odd * 10 + sorted_input[i]

    if odd == 0:
        while even > 100:
            even = even // 10

    return even, odd


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    middle_idx = len(input_list) // 2
    left = merge_sort(input_list[:middle_idx])
    right = merge_sort(input_list[middle_idx:])
    return merge(left, right)


def merge(left, right):
    merged = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] >= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    merged += left[left_idx:]
    merged += right[right_idx:]

    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

print("\n----------test cases given in the problem------------")
print("Pass if input array [1, 2, 3, 4, 5] = output array [542, 31]")
test_function([[1, 2, 3, 4, 5], [542, 31]])
print("Pass if input array [4, 6, 2, 5, 9, 8] =  output array [964, 852]")
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

print("\n-------other test cases---------------------")

print("\nPass if input array [] =  output array [0, 0]")
test_function([[], [0, 0]])
print("\nPass if input array [7] =  output array [7, 0]")
test_function([[7], [7, 0]])
print("\nPass if input array [0,9] =  output array [9, 0]")
test_function([[0,9], [9,0]])
print("\nPass if input array [9,0] =  output array [9, 0]")
test_function([[9,0], [9, 0]])

print("\nPass if input array [5, 0, 0, 0, 0, 0] =  output array [50, 0]")
test_function([[5, 0, 0, 0, 0, 0], [50, 0]])

print("\nPass if input array [1,9,8,3] =  output array [93, 81]")
test_function([[1,9,8,3], [93,81]])
print("\nPass if input array [7,8,6,1,4,3] =  output array [863,741]")
test_function([[7,8,6,1,4,3], [863,741]])

print("\n-------edge cases---------------------")
print("case where an empty array is passed")
test_function([[],[]])

print("\ncase where an array contains same digits")
test_function([[1,1],[1, 1]])

# the above test cases should print the following results
"""
----------test cases given in the problem------------
Pass if input array [1, 2, 3, 4, 5] = output array [542, 31]
Pass
Pass if input array [4, 6, 2, 5, 9, 8] =  output array [964, 852]
Pass

-------other test cases---------------------

Pass if input array [] =  output array [0, 0]
Pass

Pass if input array [7] =  output array [7, 0]
Pass

Pass if input array [0,9] =  output array [9, 0]
Pass

Pass if input array [9,0] =  output array [9, 0]
Pass

Pass if input array [5, 0, 0, 0, 0, 0] =  output array [50, 0]
Pass

Pass if input array [1,9,8,3] =  output array [93, 81]
Pass

Pass if input array [7,8,6,1,4,3] =  output array [863,741]
Pass

-------edge cases---------------------
case where an empty array is passed
Pass

case where an array contains same digits
Pass

"""

