# Countdown - Create a function that accepts a number as an input.
#   Return a new array that counts down by one, from the number
#   (as arrays 'zero'th element) down to 0 (as the last element).
#   For example countDown(5) should return [5,4,3,2,1,0].


def countDown(num):
    arr = []
    for i in range(num, -1, -1):
        arr.append(i)
    return arr


# print(countDown(5))


# Print and Return - Your function will receive an array with two numbers.
# Print the first value, and return the second.

def prtRtn(arr):
    print(arr[0])
    return arr[1]


# print(prtRtn([2, 3]))

# First Plus Length - Given an array, return the sum of the first value in the array,
#   plus the array's length.


def firstPlusLen(arr):
    sum = arr[0] + len(arr)
    return sum


# print(firstPlusLen([2, 1, 5, 2]))

# Values Greater than Second - Write a function that accepts any array,
#   and returns a new array with the array values that are greater than its 2nd value.
#   Print how many values this is.  If the array is only one element long,
#   have the function return False

def valGreaterSec(arr):
    rtnArr = []
    for i in arr:
        if i > arr[1]:
            rtnArr.append(i)
    print(len(rtnArr))
    if(len(rtnArr) == 1):
        return False
    else:
        return rtnArr


# print(valGreaterSec([1, 3, 5, 2, 6]))

# This Length, That Value - Write a function called lengthAndValue which
#   accepts two parameters, size and value. This function should take two
#   numbers and return a list of length size containing only the number in value.
#   For example, lengthAndValue(4,7) should return [7,7,7,7].

def lengthAndValue(size, value):
    arr = []
    count = 0
    while count < size:
        arr.append(value)
        count += 1
    return arr


# print(lengthAndValue(6, 17))
