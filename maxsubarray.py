import sys

def maxsubarray(arr, low, high):
    if low == high:
        return low, high, arr[low]
    mid = (low+(high-1))//2
    left_low, left_high, left_sum = maxsubarray(arr, low, mid)
    right_low, right_high, right_sum = maxsubarray(arr, mid+1, high)
    cross_low, cross_high, cross_sum = maxcrossarray(arr, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum

def maxcrossarray(arr, low, mid, high):
    left_sum = -sys.maxsize
    curr_sum = 0
    for i in range(mid, low-1, -1):
        curr_sum += arr[i]
        if curr_sum > left_sum:
            left_sum = curr_sum
            max_left = i
    right_sum = -sys.maxsize
    curr_sum = 0
    for i in range(mid+1, high+1):
        curr_sum += arr[i]
        if curr_sum > right_sum:
            right_sum = curr_sum
            max_right = i
    return max_left, max_right, left_sum+right_sum

arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(maxsubarray(arr, 0, len(arr)-1))