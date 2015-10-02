'''
Created on Jul 23, 2015

@author: nbkhzmb
'''
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    
    def maxProfit(self, prices):
        if not prices:
            return 0
        numDays = len(prices)
        if numDays == 1:
            return 0
        DFMAX = [0] * numDays
        DBMAX = [0] * numDays
        
        prev = 0
        maxProfit = 0
        for i in range(1, numDays):
            deltaPrice = prices[i] - prices[i - 1]
            curr = prev + deltaPrice
            curr = max(curr,0)
            maxProfit = max(curr, maxProfit)
            DFMAX[i] = maxProfit
            prev = curr
        
        prev = 0
        maxProfit = 0
        for j in range(numDays - 2, 0, -1):
            deltaPrice = prices[j] - prices[j + 1]
            curr = prev + deltaPrice
            curr = min(curr, 0)
            maxProfit = min(curr, maxProfit)
            DBMAX[j] = maxProfit
            prev = curr
        
        D = [-(DBMAX[i]) + DFMAX[i] for i in range(0, numDays)]
        maxProfit = 0
        for profit in D:
            if profit > maxProfit:
                maxProfit = profit
        
        return maxProfit
    
    def maxProfitBackup2(self, prices):
        if not prices:
            return 0
        numDays = len(prices)
        if numDays == 1:
            return 0
        DF = [0] * numDays
        DB = [0] * numDays
        DBMAX = [0] * numDays

        for i in range(1, numDays):
            deltaPrice = prices[i] - prices[i - 1]
            val = DF[i - 1] + deltaPrice
            DF[i] = val if val > 0 else 0
            for k in range(1, i):
                val = DB[k] + deltaPrice
                DB[k] = val if val > 0 else 0
                if DB[k] > DBMAX[k]:
                    DBMAX[k] = DB[k]
        
        maxProfit = 0
        for m in range(1, numDays):
            val = DBMAX[m] + DF[m]
            if val > maxProfit:
                maxProfit = val
        return maxProfit
    
    def maxProfitBackup(self, prices):
        if not prices:
            return 0
        numDays = len(prices)
        if numDays == 1:
            return 0
        D = []
        
        for i in range(numDays, 0, -1):
            D.append([0] * i)

        for j in range(1, numDays):
            for k in range(0, j):
                val = D[k][j - k - 1] + (prices[j] - prices[j - 1])
                D[k][j - k] = val if val > 0 else 0
        
        maxProfit = 0
        for m in range(1, numDays):
            val = D[0][m] + max(D[m])
            if val > maxProfit:
                maxProfit = val
        return maxProfit
    

def test():
    s = Solution()
    print s.maxProfit([1, 6, 4, 5, 3, 7, 2])
    print s.maxProfit([3, 6, 4, 2, 5, 7, 1])
    
def test2():
    s = Solution()

