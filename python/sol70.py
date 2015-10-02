'''
Created on Jul 22, 2015

@author: nbkhzmb
'''
class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n<2:
            return 1
        D = [0] * (n+1)
        D[0] = 1
        D[1] = 1
        for i in range(2, n+1):
            D[i] = D[i-1] + D[i-2]
        return D[n]
    
def test():
    s = Solution()
    print s.climbStairs(4)