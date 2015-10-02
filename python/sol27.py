'''
Created on Jul 22, 2015

@author: nbkhzmb
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            return nums[0] 
        D = [0] * length
        D[0] = nums[0]
        D[1] = max(nums[0], nums[1])
        for i in range(2, length):
            D[i] = max((nums[i] + D[i - 2]), D[i - 1])
        
        return D[-1]


def test():
    s = Solution()
    print s.rob([1, 6, 3, 7, 8, 4, 5])
