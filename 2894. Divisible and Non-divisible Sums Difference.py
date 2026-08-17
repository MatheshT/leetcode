'''2894. Divisible and Non-divisible Sums Difference


Example 1:

Input: n = 10, m = 3
Output: 19
Explanation: In the given example:
- Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
- Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
We return 37 - 18 = 19 as the answer.'''

#code link:https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/



class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        c=0
        d=0
        for i in range(1,n+1):
            if i%m==0:
                c+=i
            else:
                d+=i
        return d-c
