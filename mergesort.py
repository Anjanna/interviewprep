#merge sort main function
def mergesort(arr, low, high):
    if low < high:
        mid = (low+(high-1))//2
        mergesort(arr, low, mid)
        mergesort(arr, mid+1, high)
        merge(arr, low, mid, high)

#function to merge the subarrays
def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
    a = [0] * n1
    b = [0] * n2
    for i in range(0, n1):
        a[i] = arr[low + i]
    for i in range(0, n2):
        b[i] = arr[mid + i + 1]
    i = 0
    j = 0
    k = low
    while i < n1 and j < n2:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = b[j]
        k += 1
        j += 1

arr = [4,20,14,1,15,3,33,5]
mergesort(arr, 0, len(arr)-1)
print(arr)

