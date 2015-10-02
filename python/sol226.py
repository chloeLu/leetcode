# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return
        if root.left or root.right:
            root.left, root.right = root.right, root.left
        
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root
            
        
def printTree(t):
    if not t:
        print "[]"
        return
    layer = [t]
    while layer:
        nextLayer = []
        layerStr = ""
        for t in layer:
            layerStr = layerStr + str(t.val) + " " 
            if t.left:
                nextLayer.append(t.left)
            if t.right:
                nextLayer.append(t.right)
        print layerStr
        layer = nextLayer
        
def testPrint():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    
    node1.left = node2
    node1.right = node3
    printTree(None)
    printTree(node1)

def test():
    s = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    s.invertTree(node1)
    printTree(node1)

def test1():
    s = Solution()
    node1 = TreeNode(1)
    s.invertTree(node1)
    printTree(node1)

