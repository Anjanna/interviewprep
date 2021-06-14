import sys

class Heap:
    def __init__(self, length=None, heap_size=None):
        self.length = length
        self.heap_size = heap_size

    def max_heapify(self, arr, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and arr[l] > arr[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            self.swap(arr, i, largest)
            self.max_heapify(arr, largest)
    
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    
    def build_max_heap(self, arr):
        self.length = len(arr)
        self.heap_size = len(arr)
        for i in range((len(arr)//2)-1, -1, -1):
            self.max_heapify(arr, i)
    
    def left(self, i):
        return 2*i+1
    
    def right(self, i):
        return self.left(i) + 1
    
    def parent(self, i):
        return (i-1)//2
    
    def heap_sort(self, arr):
        self.build_max_heap(arr)
        for i in range(len(arr)-1, 0, -1):
            self.swap(arr, 0, i)
            self.heap_size -= 1
            self.max_heapify(arr,0)
    
    def extract_max(self, arr):
        heapmax = arr[0]
        arr[0] = arr[self.heap_size-1]
        self.heap_size -= 1
        self.max_heapify(arr, 0)
        return heapmax

    def increase_key(self, arr, i, key):
        if arr[i] > key:
            return "invalid key"
        arr[i] = key
        while i > 0 and arr[self.parent(i)] < arr[i]:
            self.swap(arr, self.parent(i), i)
            i = self.parent(i)
    
    def heap_insert(self, arr, key):
        self.heap_size += 1
        arr[self.heap_size-1] = -sys.maxsize
        self.increase_key(arr, self.heap_size-1, key)

arr = [4,20,14,1,15,3,33,5]
heap = Heap()
heap.build_max_heap(arr)
print("heap built")
print(arr)
print('extracting max')
print(heap.extract_max(arr))
print('array after extract max')
print(arr)
print('inserting 70')
heap.heap_insert(arr, 70)
print(arr)
print('increasing 15 to 16')
heap.increase_key(arr, 3, 16)
print(arr)