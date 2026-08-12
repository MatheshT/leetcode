'''9. Palindrome Number


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.'''


#code link : https://leetcode.com/problems/palindrome-number/description/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        d=s[::-1]
        if s==d:
            return True
        else:
            return False
