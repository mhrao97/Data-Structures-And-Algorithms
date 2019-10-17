# Problem 1: Square Root of an Integer
"""
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
"""

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
        return number

    # handle negative numbers. Sqrt of negative number is -1 times sqrt of number. square root of -1 is imaginary
    # https://www.khanacademy.org/math/algebra2/introduction-to-complex-numbers-algebra-2/the-imaginary-numbers-algebra-2/v/imaginary-roots-of-negative-numbers
    if number < 0:
        print("\nSquare root of negative number is square root of -1 * sqrt(", (-1*number), ") which is -1 *")
        return sqrt(-1*number)

    # using Binary search to find the square root
    begin = 1
    end = number
    result = 1

    while (begin <= end):
        mid = (begin + end) // 2

        # if number is a perfect square
        if mid * mid == number:
            return mid

        # if mid * mid is smaller than number
        if (mid * mid < number):
            begin = mid + 1
            result = mid
        else:
            # if mid*mid is greater than number
            end = mid - 1

    return result

print("\n--- test cases given in the problem ---")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print("\n----edge cases---")
print("square root of 0 is ", sqrt(0))
print(sqrt(-1))
print(sqrt(-52))

print("\n-----other tests-----")
print("square root of 121 is",sqrt(121))
print("square root of 15625 is",sqrt(15625))

# the above test cases should print the following result:
"""

--- test cases given in the problem ---
Pass
Pass
Pass
Pass
Pass

----edge cases---
square root of 0 is  0

Square root of negative number is square root of -1 * sqrt( 1 ) which is -1 *
1

Square root of negative number is square root of -1 * sqrt( 52 ) which is -1 *
7

-----other tests-----
square root of 121 is 11
square root of 15625 is 125

"""