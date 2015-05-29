'''
Created on May 27, 2015
https://leetcode.com/problems/reverse-integer/
Note: 
Python has no overflow problems, so line24-28 isnt needed. Yet I added them for the case for letting test cases pass
@author: Chloe Lu
'''
import sys
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        val = 0
        
        if x > 0:
            val = int(str(x)[::-1])
        elif x == 0:
            return 0
        elif x < 0:
            val = -int(str(0 - x)[::-1])
        
        print sys.maxint
        
        if not -sys.maxint-1 <= val <= sys.maxint:
            return 0
        else:
            return val


def test1():
    print Solution().reverse(1534236469)
