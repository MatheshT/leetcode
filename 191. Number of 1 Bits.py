'''191. Number of 1 Bits


Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.'''

#code link: https://leetcode.com/problems/number-of-1-bits/description/



class Solution:
    def hammingWeight(self, n: int) -> int:
        c=bin(n)

        return c.count("1")
