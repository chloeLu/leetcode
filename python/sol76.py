'''
Created on Oct 2, 2015

@author: nbkhzmb
'''
from os.path import sys
import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # build the initial queue
        tCharCountDict = {}
        for cT in t:
            if not cT in tCharCountDict:
                tCharCountDict[cT] = 1
            else:
                tCharCountDict[cT] += 1
        
        tCharDequeDict = {}
        minWindow = (sys.maxsize, -1)  # length, startIdx
        count = 0
        for sIdx, sChar in enumerate(s):
            if sChar in tCharCountDict:
                idxCharTuple = (sIdx, sChar)
                if sChar not in tCharDequeDict:
                    tCharDequeDict[sChar] = collections.deque()
                    count +=1
                elif len(tCharDequeDict[sChar]) != tCharCountDict[sChar]:
                    count +=1
                else:
                    #print (tCharDequeDict)
                    tCharDequeDict[sChar].popleft()
                tCharDequeDict[sChar].append(idxCharTuple)
                
                # only carry out this step when the entire t is counted
                if count == len(t):
                    minIdx = sys.maxsize
                    for key in tCharDequeDict:
                        minIdx = min(minIdx, tCharDequeDict[key][0][0])
                    minWindow = min(minWindow, (sIdx - minIdx, minIdx))
                    #print (minWindow)
        
        if (minWindow[1] == -1):
            return ""
        else:
            return s[minWindow[1]:minWindow[0] + minWindow[1] + 1]

def test():
    s = Solution()
    print (s.minWindow("ADOBECODEBANC", "ABC"))
    print (s.minWindow("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB", "AB"))