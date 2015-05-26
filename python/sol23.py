'''
Created on May 18, 2015
https://leetcode.com/problems/merge-k-sorted-lists/
@author: Chloe Lu
'''
import Queue

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        if not lists:
            return []
        lists = filter(None, lists)
        pq = Queue.PriorityQueue()
        rlNode = ListNode(0)
        rlHead = rlNode
        for listNode in lists:
            pq.put((listNode.val, listNode,))
        
        while not pq.empty():
            tupleOut = pq.get()
            if tupleOut[1].next:
                pq.put((tupleOut[1].next.val, tupleOut[1].next,))
            rlNode.next = tupleOut[1]
            rlNode = rlNode.next
            rlNode.next = None
        
        return rlHead.next