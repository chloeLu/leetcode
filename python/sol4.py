'''
Created on May 13, 2015

@author: nbkhzmb
'''
class Solution:
    '''
    https://leetcode.com/problems/median-of-two-sorted-arrays/
    '''
    
    # @param {integer} x
    # @return {boolean}
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        # swap and always let num1 pointing to the smaller array
        # print str(len1) + " " + str(len2)
        if len1 > len2:
            len1, len2 = len2, len1
            nums1, nums2 = nums2, nums1
            
        # boundary case: nums1 has no element. not possible for num2 to have no element
        if len1 == 0 :
            if (len2) % 2 == 1:
                return nums2[int((len2 - 1) / 2)]
            else:
                return float((nums2[int((len2 - 1) / 2)] + nums2[int((len2 - 1) / 2 + 1)])) / 2
        
        # idx1, idx2: starting index in nums1 and nums2. 
        # Note: if both idx1 and idx2 has even numbers.. idx2 ++
        idx1 = int((len1 - 1) / 2);
        idx2 = int((len2 - 1) / 2);
        if len1 % 2 == 0 and len2 % 2 == 0:
            idx2 += 1
        
        # chop is how many elements that should be subtracted from one idx and added to another idx
        chop = int(idx1 / 2);
        # boundary: chop shouldnt start with being 0
        if (chop == 0): chop = 1 
        
        while(not(idx1 < 0 or idx2 < 0)):
            if(not(idx1 == len1 - 1) and nums1[idx1 + 1] < nums2[idx2]):
                idx1 += chop;
                idx2 -= chop;
            elif(not(idx2 == len2 - 1) and nums2[idx2 + 1] < nums1[idx1]):
                idx1 -= chop;
                idx2 += chop;
            else:
                break
            
            chop = int(chop / 2);
            if (chop == 0): chop = 1
        
        mid1 = 0
        mid2 = 0
        if (idx1<0):
            mid2 = nums2[idx2]
            mid1 = nums2[idx2-1]
        elif (nums1[idx1] > nums2[idx2]):
            mid2 = nums1[idx1]
            mid1 = nums2[idx2] if idx1 < 1  else max(nums1[idx1 - 1], nums2[idx2])
        else:
            mid2 = nums2[idx2]
            mid1 = nums1[idx1] if idx2 < 1  else max(nums1[idx1], nums2[idx2 - 1])
        
        if (len1 + len2) % 2 == 1:
            return mid2
        else:
            return float(mid1 + mid2) / 2
        
    def __init__(self):
        '''
        Constructor
        '''
        print(self.findMedianSortedArrays([], [1]))
