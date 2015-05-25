'''
Created on May 19, 2015

@author: Chloe Lu
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class BSTIterator:
    # @param root, a binary search tree's root node
    trace=deque()
    
    def __init__(self, root):
        if root:
            self.updateTrace(root)
    
    def updateTrace(self, root):
        self.trace.appendleft(root)
        while root.left:
            self.trace.appendleft(root.left)
            root = root.left
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return bool(self.trace)

    # @return an integer, the next smallest number
    def next(self):
        if not self.trace:
            return None
        node = self.trace[0]
        del self.trace[0]
        if node.right:
            self.updateTrace(node.right)
        return node.val


def test():
    n1=TreeNode(1)
    n2=TreeNode(2)
    n3=TreeNode(3)
    n4=TreeNode(4)
    n5=TreeNode(5)
    n6=TreeNode(6)
    n7=TreeNode(7)
    n8=TreeNode(8)
    n9=TreeNode(9)
    n8.left=n5
    n8.right=n9
    n5.left=n4
    n5.right=n7
    n7.left=n6
    n4.left=n2
    n2.left=n1
    n2.right=n3
    i= BSTIterator(n8)
    while i.hasNext(): print (i.next().val)

def test1(): 
    i= BSTIterator(None)
    while i.hasNext(): print (i.next().val)
    
def test2():
    n8=TreeNode(8)
    n9=TreeNode(9)
    n8.right=n9
    i= BSTIterator(n8)
    while i.hasNext(): print (i.next().val)
def test3():
    n8=TreeNode(8)
    i= BSTIterator(n8)
    while i.hasNext(): print (i.next().val)
            

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())