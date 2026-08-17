''' 1929. Concatenation of Array



Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]'''

#code link:https://leetcode.com/problems/concatenation-of-array/description/



class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
       return nums + nums
