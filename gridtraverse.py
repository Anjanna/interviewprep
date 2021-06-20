"""
Traverse a grid of size m,n. Find the number of ways
to traverse the grid from the start to the end.
You can only move down and right.
"""

def gridtraverse(m, n, memo = {}):

    key = str(m) + ','+ str(n)

    if key in memo:
        return memo[key]
    
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    
    memo[key] = gridtraverse(m-1, n) + gridtraverse(m, n-1)

    return memo[key]

print(gridtraverse(18,18))