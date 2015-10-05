'''
Created on Oct 5, 2015

@author: nbkhzmb
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        iDict = {}
        for idx, num in enumerate(nums):
            if (num not in iDict):
                iDict[num] = idx
            else:
                if (idx-iDict[num]) <=k:
                    return True
                else:
                    iDict[num] = idx
        return False