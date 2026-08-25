'''367. Valid Perfect Square


Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.'''


#code link:https://leetcode.com/problems/valid-perfect-square/description/



class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(int(num)):
            if i*i==num:
                return True
                
            if i*i>num:
                break
        return False
        
