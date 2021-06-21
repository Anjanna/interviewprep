"""
Given an array of numbers and a target sum.
Return any array of numbers from the original array
if target sum can be acheived. Else return NULL.
"""

def howsum(target, arr, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for num in arr:
        remainder = target - num
        result = howsum(remainder, arr, memo)
        if result is not None:
            memo[target] = result + [num]
            return memo[target]
    memo[target] = None
    return None

print(howsum(7, [2,3])) #[3,2,2]
print(howsum(7, [5,3,4,7], {})) #[4,3]
print(howsum(300, [7,14])) #None