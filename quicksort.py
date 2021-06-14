def quicksort(arr, low, high):
    if low < high:
        q = partition(arr, low, high)
        quicksort(arr, low, q-1)
        quicksort(arr, q+1, high)

def partition(arr, low, high):
    x = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= x:
            i += 1
            swap(arr, i, j)
    swap(arr, i+1, high)
    return i+1

def swap(arr, a, b):
    t = arr[a]
    arr[a] = arr[b]
    arr[b] = t

arr = [4,20,14,1,15,3,33,5]
quicksort(arr, 0, len(arr)-1)
print(arr)