class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        prevLow=prices[0]
        prevHigh=prices[0]
        maxSum=0
        prices = [prices[0]] + prices
        
        for p in prices:
            if p > prevHigh:
                prevHigh = p
            elif p < prevHigh:
                maxSum += (prevHigh - prevLow)
                prevLow = p
                prevHigh = p
        maxSum += (prevHigh - prevLow)
        return maxSum

def test():
    s = Solution()
    print (s.maxProfit([0,2,1,4,3,6,5,7,2]))
    print (s.maxProfit([1,2]))
        