'''
Created on May 18, 2015
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
@author: Chloe Lu
'''
import Queue

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return 
        
        nodeList = [(root, 0,)]
        while nodeList:
            nodeTuple = nodeList[0]
            del nodeList[0]
            node = nodeTuple[0]
            layer = nodeTuple[1]
            if nodeList:
                nextTuple = nodeList[0]
                if (nextTuple[1]==nodeTuple[1]):
                    node.next = nextTuple[0]
            if node.left:
                nodeList.append((node.left, layer+1,))
            if node.right:
                nodeList.append((node.right, layer+1,))
        
    def printTree(self, root):
        layerQ = Queue.Queue()
        layerQ.put(root)
        while not layerQ.empty():
            node = layerQ.get()
            if node:
                if node.left:
                    layerQ.put(node.left)
                else:
                    layerQ.put(None)
                if node.right:
                    layerQ.put(node.right)
                else:
                    layerQ.put(None)
                
                if node.next:
                    print "(" + str(node.val) + "," + str(node.next.val) + ")"
                else:
                    print "(" + str(node.val) + ",#)"
                
    def __init__(self):
        '''
        Constructor
        '''
        node1 = TreeLinkNode(1)
        node2 = TreeLinkNode(2)
        node3 = TreeLinkNode(4)
        node1.left = node2
        node2.right = node3
        
        self.connect(node1)
        self.printTree(node1)
