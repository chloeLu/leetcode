'''
Created on Sep 30, 2015

@author: nbkhzmb
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if (m==0 or n==0):
            return 0
        if (m==1 or n==1):
            return 1
        if (m==2):
            return n
        elif (n==2):
            return m
        
        D=[[1 for x in range(n)] for x in range(m)]
        for row in range(1,m):
            for col in range(1,n):
                D[row][col] = D[row-1][col] + D[row][col-1]
        
        return D[m-1][n-1]

def test():
    s = Solution()
    print s.uniquePaths(1, 9)
    print s.uniquePaths(9, 1)
    print s.uniquePaths(3, 3)
        