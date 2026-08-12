'''3783. Mirror Distance of an Integer



Example 1:

Input: n = 25

Output: 27

Explanation:

reverse(25) = 52.
Thus, the answer is abs(25 - 52) = 27'''''




#code line:https://leetcode.com/problems/mirror-distance-of-an-integer/description/




class Solution:
    def mirrorDistance(self, n: int) -> int:
        s=str(n)
        d=int(s[::-1])
        c=n-d
        return abs(c)

        
