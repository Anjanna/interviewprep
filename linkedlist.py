class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Linkedlist:
    def __init__(self, head=None):
        self.head = head
    
    def display(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

    def removeduplicates(self):
        unique = {}
        curr = self.head
        prev = curr
        while curr:
            if curr.value not in unique:
                unique[curr.value] = 1
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next
    
    def ktolast(self, k):
        curr = self.head
        prev = curr
        i = 0
        while curr:
            if i <= k:
                i += 1
            else:
                prev = prev.next
            curr = curr.next
        if (i-1) != k:
            print("invalid input")
        else:
            print(prev.value)

node = Node(5, Node(3, Node(3, Node(2, Node(20, Node(12, Node(1, Node(1))))))))
ll = Linkedlist(node)
ll.ktolast(7)
