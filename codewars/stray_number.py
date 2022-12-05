# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
#
# Complete the method which accepts such an array, and returns that single different number.
#
# The input array will always be valid! (odd-length >= 3)

def stray(arr) -> int:
    stray_num = 0
    for item in arr:
        if arr.count(item) == 1:
            stray_num = item
            print(stray_num)
            break
    return stray_num


stray([1, 2, 3, 3, 2, 1, 9])
