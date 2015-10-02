'''
Created on Jun 22, 2015
https://leetcode.com/problems/subsets-ii/
@author: nbkhzmb
'''
import copy
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        if not nums:
            return []
        nums.sort()
        result = self.subsetsNoEmpty(nums)
        result.append([])
        return result
    
    def subsetsNoEmpty(self, nums):
        # boundary case
        if len(nums) == 1:
            return [nums]
        elif len(nums) == 2:
            return [[nums[0]], [nums[1]], nums]
        
        # recursion and merge
        len1 = len(nums)/2
        
        result1=self.subsetsNoEmpty(nums[0:len1])
        result2=self.subsetsNoEmpty(nums[len1:])
        result = list(result1)
        result.extend(list(result2))
        for y in result2:
            temp1 = copy.deepcopy(result1)
            [x.extend(y) for x in temp1]
            result.extend(temp1)
        return result
    

def test():
    s = Solution()
    print s.subsets([4,1,0])

def test1():
    s = Solution()
    print s.subsets([])