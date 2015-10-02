'''
Created on Sep 30, 2015

@author: nbkhzmb
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        D = [0] * (rowIndex+1)
        D[0] = 1
        idx = 1
        while (idx <= rowIndex):
            D[idx] = D[idx - 1] * (rowIndex + 1 - idx) / idx
            idx = idx + 1
        return D

def test():
    s = Solution()
    print s.getRow(4)
