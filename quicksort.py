class Sort:
    def quicksort(self,a,p,r):
        if p < r:
            q = self.hoarePartition(a,p,r)
            self.quicksort(a,p,q-1)
            self.quicksort(a,q+1,r)
    
    def partition(self,a,p,r):
        i=p-1
        x=a[r]
        for j in range(p,r):
            if a[j] <= x:
                i+=1
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
        temp = a[i+1]
        a[i+1] = a[r]
        a[r] = temp
        return i+1
    
    def hoarePartition(self,a,p,r):
        x=a[p]
        i=p
        j=r
        while 1:
            while a[j] > x:
                j-=1
            while a[i] < x:
                i+=1
            if i < j:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
            else:
                return j

arr = [2,8,7,1,3,5,6,4]
Sort().quicksort(arr,0,len(arr)-1)
print(arr)