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
        if numDays==1:
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

    