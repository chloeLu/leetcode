'''
Created on May 26, 2015
https://leetcode.com/problems/largest-rectangle-in-histogram/
This solution is.... ugly.. check out perfect solution here https://leetcode.com/discuss/12780/my-concise-c-solution-ac-90-ms
@author: nbkhzmb
'''
from collections import deque
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        if not height:
            return 0
        maxArea = 0
        stack = []
        sectionStartIdx = 0
        for idx, h in enumerate(height):
            appendIdx = idx
            if stack:
                if stack[0][0] > h:
                    firstColArea = (idx - sectionStartIdx) * stack[0][0]
                    maxArea = max(maxArea, firstColArea, self.largestRecGivenIncreasingStack(stack))
                    stack = []
                elif stack[-1][0] > h:
                    q = deque()
                    q.appendleft(stack.pop())
                    while stack and stack[-1][0] > h :
                        q.appendleft(stack.pop())
                    maxArea = max(maxArea, self.largestRecGivenIncreasingStack(q))
                    appendIdx = stack[-1][2] + 1
                    
            # update stack and sectionStartIdx
            if h == 0:
                sectionStartIdx = idx + 1
            else:
                stack.append((h, appendIdx, idx,));
        # lastly, if stack not empty, calculate area and update maxArea
        # this deals with case where lowest column is not the first
        if stack:
            area = (len(height) - sectionStartIdx) * stack[0][0]
            for t in stack:
                area = max(area, (len(height) - t[1]) * t[0])
            maxArea = max(maxArea, area)
        return maxArea
    
    def largestRecGivenIncreasingStack(self, stack):
        maxArea = 0
        if stack:
            # print stack
            lastIdx = stack[-1][2]
            for t in stack:
                maxArea = max(maxArea, (lastIdx - t[1] + 1) * t[0])
        return maxArea
def test():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    
def test1():
    height = [0, 9]
    print Solution().largestRectangleArea(height)
def test2():
    height = [2, 1, 2]
    print Solution().largestRectangleArea(height)
def test3():
    height = [0, 3, 2, 5]
    print Solution().largestRectangleArea(height)
def test4():
    height = [5, 4, 4, 6, 3, 2, 9, 5, 4, 8, 1, 0, 0, 4, 7, 2]
    print Solution().largestRectangleArea(height)       
def test5():
    height = [1, 2, 2]
    print Solution().largestRectangleArea(height)
def test6():
    height = [3, 6, 5, 7, 4, 8, 1, 0]
    print Solution().largestRectangleArea(height)
def test7():
    height = [2, 7, 6, 7, 8, 6, 6, 3, 0, 2]
    print Solution().largestRectangleArea(height)   
def test8():
    height = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]
    print Solution().largestRectangleArea(height)   
def test9():
    height = [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]
    print Solution().largestRectangleArea(height)   
def test10():
    height = [1, 4, 5, 3, 2, 7, 5, 3, 0]
    print Solution().largestRectangleArea(height)   
                        

