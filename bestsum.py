"""
Given an array of numbers and a target sum.
Return the shortest array of numbers from the original array
if target sum can be acheived. Else return NULL.
"""

def bestsum(target, arr, memo={}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    shortest = None
    for num in arr:
        remainder = target - num
        result = bestsum(remainder, arr)
        if result is not None:
            combination = result + [num]
            if not shortest or len(combination) < len(shortest):
                shortest = combination
    memo[target] = shortest
    return shortest

print(bestsum(7, [5,3,4,7])) #[7]
print(bestsum(8, [2,3,5])) #[3,5]
print(bestsum(100, [1,2,5,25])) #[25,25,25,25]