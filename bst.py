class Solution:
    def searchRecursive(self, node, key):
        if not key or node.value == key:
            return node
        if key < node.value:
            return self.searchRecursive(node.left, key)
        return self.searchRecursive(node.right, key)
    
    def searchIterative(self, node, key):
        if not node:
            return None
        if node.value == key:
            return node
        while node and key != node.value:
            if key > node.value:
                node = node.right
            else:
                node = node.left
        return node
    
    def minimumRecursive(self, node):
        if not node:
            return None
        while node.left:
            node = node.left
        return node

class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

class BST:
    def __init__(self):
        self.root = None

    def inorder(self):
        self._inOrderRecursive(self.root)

    def _inOrderRecursive(self, node):
        if node:
            self._inOrderRecursive(node.left)
            print(node.value)
            self._inOrderRecursive(node.right)
    
    def insert(self, node):
        y = None
        x = self.root
        while(x):
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if not y:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node
    
    def mininum(self):
        if self.root:
            return self._mininumHelper(self.root)
    
    def _mininumHelper(self, node):
        while node.left:
            node = node.left
        return node
    
    def successor(self, node):
        if not node:
            return None
        if node.right:
            return self._mininumHelper(node.right)
        y = node.parent
        while y and node == y.right:
            node = y
            y = y.parent
        return y
    
    def _transplant(self, u, v):
        if not u.parent:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v:
            v.parent = u.parent

    def delete(self, node):
        if not node.left:
            self._transplant(node, node.right)
        elif not node.right:
            self._transplant(node, node.left)
        else:
            y = self._mininumHelper(node.right)
            if y.parent != node:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y

    
bst = BST()
bst.insert(Node(12))
bst.insert(Node(5))
node18 = Node(18)
bst.insert(node18)
bst.insert(Node(2))
bst.insert(Node(9))
node15 = Node(15)
bst.insert(node15)
bst.insert(Node(19))
node17 = Node(17)
bst.insert(node17)
bst.delete(node18)
bst.inorder()

