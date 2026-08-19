'''3024. Type of Triangle


Example 1:

Input: nums = [3,3,3]
Output: "equilateral"
Explanation: Since all the sides are of equal length, therefore, it will form an equilateral triangle.'''

#code link:https://leetcode.com/problems/type-of-triangle/description/



class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        n=sorted(nums)
        a,b,c=n
        if a+b <=c:
            return "none"
        elif a==b==c:
            return "equilateral"
        elif a==b or b==c or a==c:
            return "isosceles"
        else:
            return "scalene"
