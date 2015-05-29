'''
Created on May 29, 2015
https://leetcode.com/problems/regular-expression-matching/
@author: Chloe Lu
'''

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    
    count = 0
    def isMatch(self, s, p):
        if self.count > 80:
            print "Failure!!!"
            return False
        self.count += 1
        sIdx = 0
        for idx, ch in enumerate(p):
            if ch == "*":
                continue
            if sIdx >= len(s):
                return False
            isGreedyCh = True if (idx < len(p) - 1 and p[idx + 1] == "*") else False
            if not isGreedyCh:
                if not self.isCharPerfectMatch(s[sIdx], ch):
                    return False
                else:
                    sIdx += 1
            else:
                # greedy unless fail
                greedySIdx = sIdx
                gch = ch
                if self.isCharPerfectMatch(s[sIdx], ch):
                    gch = s[sIdx]
                while (greedySIdx < len(s) and self.isCharPerfectMatch(s[greedySIdx], gch)):
                    greedySIdx += 1
                    
                # end of s and end of p
                if greedySIdx == len(s) and idx == len(p) - 2:
                    return True
                
                print "idx:" + str(idx) + "; greedySIdx:" + str(greedySIdx)
                while greedySIdx >= sIdx:
                    print "test: " + s[greedySIdx:] + "   " + p[idx+2:]
                    if self.isMatch(s[greedySIdx:], p[idx+2:]):
                        return True
                    else:
                        greedySIdx -= 1
                return False
        return sIdx >= len(s)
    def isCharPerfectMatch(self, c, p):
        if p != "." and c != p:
            return False
        return True
            
def test1():
    print Solution().isMatch('aa', 'a')
    print Solution().isMatch('aa', 'aa')
    print Solution().isMatch('aaa', 'aa')
    print Solution().isMatch('aa', 'a*')
    print Solution().isMatch('aa', '.*')
    print Solution().isMatch('ab', '.*')
    print Solution().isMatch('aab', 'c*a*b')

def test2():
    print Solution().isMatch('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c')
    
            
            
                    
