'''1281. Subtract the Product and Sum of Digits of an Integer



Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:'''


#code link:https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/




class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = list(map(int,str(n)))
        b = math.prod(a)
        c = sum(a)
        return b - c
