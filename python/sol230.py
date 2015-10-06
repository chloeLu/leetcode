'''
Created on Oct 6, 2015

@author: nbkhzmb
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = [0]
        targetNode = []
        self.countNodes(root, count, k, targetNode)
        return targetNode[0].val
    def countNodes(self, root, count, k, targetNodeRef):
        #print("root:" + str(root.val) + "count:" + str(count))
        if count[0] >= k:
            return
        if not root.left and not root.right:
            count[0] += 1
            if count[0] == k:
                targetNodeRef.append(root)
        else:
            if root.left:
                self.countNodes(root.left, count, k, targetNodeRef)
            if count[0] == k - 1:
                targetNodeRef.append(root)
            count[0] += 1
            if root.right:
                self.countNodes(root.right, count, k, targetNodeRef)

def test():
    node4 = TreeNode(4)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node7 = TreeNode(7)
    node11 = TreeNode(11)
    node15 = TreeNode(15)
    node8 = TreeNode(8)
    node4.left = node3
    node4.right = node7
    node3.left = node1
    node3.right = node2
    node7.right = node11
    node11.left = node8
    node11.right = node15
    
    s = Solution()
    print (s.kthSmallest(node4, 5))
    
