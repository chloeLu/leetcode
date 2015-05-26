'''
Created on May 18, 2015
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
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
        
        layerQ = Queue.Queue()
        layerQ.put(root)
        nodeList = [TreeLinkNode(0)]
        while not layerQ.empty():
            node = layerQ.get()
            if node.left:
                layerQ.put(node.left)
                layerQ.put(node.right)
            nodeList.append(node)
        
        if len(nodeList) <=2:
            return 
        exp = 1
        startIdx = 2
        endIdx = 3
        while(startIdx < len(nodeList)):
            for i in range(startIdx, endIdx):
                nodeList[i].next = nodeList[i + 1]
            exp += 1
            startIdx = 2 ** exp
            endIdx = 2 ** (exp + 1) - 1
    
    def printTree(self,root):
        layerQ = Queue.Queue()
        layerQ.put(root)
        while not layerQ.empty():
            node = layerQ.get()
            if node.left:
                layerQ.put(node.left)
                layerQ.put(node.right)
                
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
        node3 = TreeLinkNode(3)
        node1.left = node2
        node1.right = node3
        
        self.printTree(self.connect(node1))
