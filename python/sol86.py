'''
Created on May 15, 2015

@author: Chloe Lu
'''
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        # boundary case: list has only 1 element
        if head is None:
            return None;
        node = head.next
        newListNode = ListNode(0)
        newListHead = newListNode
        if head.val < x:
            newListNode.next = head
            newListNode = newListNode.next
            prevNode  = None
            head = head.next
        else:
            prevNode = head
            
        
        while(node is not None):
            nextNode = node.next
            if node.val < x:
                newListNode.next = node
                newListNode = newListNode.next
                if prevNode is not None:
                    prevNode.next = nextNode
                if head == node:
                    head = node.next
            else:
                prevNode = node
            node = nextNode
        newListNode.next = head
        return newListHead.next
