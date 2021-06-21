"""
Given an array of numbers and a target sum.
Return true if the target sum can be achieved
using the array of numbers.
"""
def cansum(target, arr, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for num in arr:
        remainder = target - num
        if cansum(remainder, arr):
            memo[target] = True
            return True
    memo[target] = False
    return False

print(cansum(7, [2,3])) #true
print(cansum(300, [7,14])) #false
print(cansum(8, [2,3,5])) #true