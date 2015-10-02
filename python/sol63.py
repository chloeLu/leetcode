'''
Created on Sep 30, 2015

@author: nbkhzmb
'''
import sets
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if (m == 0 or n == 0):
            return 0
        
        # init D
        D = [[0 for x in range(n)] for x in range(m)]
        for rIdx, aRow in enumerate(obstacleGrid):
            if aRow[0] == 0:
                D[rIdx][0] = 1
            else:
                break;
        for cIdx, element in enumerate(obstacleGrid[0]):
            if element == 0:
                D[0][cIdx] = 1
            else:
                break;
        if m == 1:
            return D[0][n - 1]
        if n == 1:
            return D[m - 1][0]
        
        for row in range(1, m):
            for col in range(1, n):
                D[row][col] = 0 if obstacleGrid[row][col]==1 else D[row - 1][col] + D[row][col - 1]
        
        return D[m - 1][n - 1]


def test():
    s = Solution()
    obs = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print s.uniquePathsWithObstacles(obs)
    obs = [[0, 0, 0]]
    print s.uniquePathsWithObstacles(obs)
    obs = [[0, 1, 0]]
    print s.uniquePathsWithObstacles(obs)
    obs = [[0], [0], [0]]
    print s.uniquePathsWithObstacles(obs)
    obs = [[0], [1], [0]]
    print s.uniquePathsWithObstacles(obs)
