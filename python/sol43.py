'''
Created on May 25, 2015
https://leetcode.com/problems/multiply-strings/
@author: nbkhzmb
'''
import itertools
class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        if int(num1) == 0 or int(num2) == 0:
            return '0'
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        # reverse string, convert each char to int
        num1 = num1[::-1]
        num2 = num2[::-1]
        num1 = map(lambda s:int(s), num1)
        num2 = map(lambda s:int(s), num2)
        
        result = []
        initialProduct = []
        carryOver = 0
        for idx in range(0, len(num2)):
            mul = num2[idx]
            product = list(initialProduct)
            for digit in num1:
                digitProduct = mul * digit + carryOver
                product.append(digitProduct % 10)
                carryOver = int(digitProduct / 10)
            initialProduct.append(0)
            if carryOver > 0:
                product.append(carryOver)
                carryOver = 0
            result = map(sum, itertools.izip_longest(result, product, fillvalue=0))
        
        # process result
        carryOver = 0
        for idx, val in enumerate(result):
            if carryOver > 0:
                val += carryOver
            if val > 10:
                result[idx] = val % 10
                carryOver = int(val / 10)
            elif val == 10:
                result[idx] = 0
                carryOver = 1
            else:
                result[idx] = val
                carryOver = 0
        if carryOver > 0:
            result.append(carryOver)
        result = result[::-1]
        return ''.join(map(str, result))

def test1():
    s = Solution()
    r = s.multiply('140', '721')
    print r
