'''
Created on Jul 24, 2015

@author: nbkhzmb
'''
class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        if not prices:
            return 0
        if k == 0:
            return 0
        elif k == 1:
            return self.maxProfitK1(prices)
        elif k == 2:
            return self.maxProfitK2(prices)
        else:
            numDays = len(prices)
            D = [[0] * numDays] * numDays
             
            
    
    def maxProfitK1(self, prices):
        numDays = len(prices)
        if numDays == 1:
            return 0
        D = [0] * numDays
        D[0] = 0
        for i in range(1, numDays):
            val = D[i - 1] + (prices[i] - prices[i - 1])
            D[i] = val if val > 0 else 0
        # find maxProfit
        maxProfit = 0
        for p in D:
            if p > maxProfit:
                maxProfit = p
        return maxProfit
    
    def maxProfitK2(self, prices):
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
            curr = max(curr, 0)
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
