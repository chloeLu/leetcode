'''
Created on May 15, 2015

@author: Chloe Lu
'''
class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, x):
        
        idx = 0;
        result = [0, 0, 0];
        while (idx < len(x) and (result[0] / 2 < len(x) - idx)):
            fold = self.foldOdd(x, idx);
            if(fold[0] > result[0]):
                result = fold;
                
            if (idx != len(x) - 1 and x[idx] == x[idx + 1]):  # omit the last char
                fold = self.foldEven(x, idx);
                if(fold[0] > result[0]):
                    result = fold;
            idx += 1;
        
        return x[result[1]:result[2] + 1];

    def foldOdd(self, inStr, idx):
        left = idx;
        right = idx;
        while(left >= 0 and right < len(inStr) and inStr[left] == inStr[right]):
            left -= 1;
            right += 1;
        right -= 1;
        left += 1;
        return [right - left + 1, left, right];
    
    def foldEven(self, inStr, idx):
        left = idx - 1;
        right = idx + 2;
        while(left >= 0 and right < len(inStr) and inStr[left] == inStr[right]):
            left -= 1;
            right += 1;
        right -= 1;
        left += 1;
        return [right - left + 1, left, right];
