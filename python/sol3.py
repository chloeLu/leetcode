'''
Created on May 15, 2015
https://leetcode.com/problems/longest-substring-without-repeating-characters/
@author: Chloe Lu
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        # boundary cases: s is empty or has only 1 char
        if len(s) == 0:
            return 0;
        elif len(s) == 1:
            return 1;
        
        # start while loop from the 2nd character
        length = 1;
        resultLen = 1
        nextCharIdx = 1
        for idx in range(0, len(s)):
            length = length - 1 if length > 1 else length
            startStr = s[idx:idx + length]
            nextCharIdx = idx + length
            #print "startStr:" + startStr + " nextCharIdx:" + str(nextCharIdx)
            while(nextCharIdx < len(s) and s[nextCharIdx] not in startStr):
                startStr += s[nextCharIdx]
                nextCharIdx += 1
                length += 1
            if (length > resultLen):
                resultLen = length
            #print("length: " + str(length))
        return resultLen;
    
    def __init__(self):
        '''
        Constructor
        '''
        print(self.lengthOfLongestSubstring("cdd"))
