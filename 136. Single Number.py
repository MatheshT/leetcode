'''136. Single Number

Example 1:

Input: nums = [2,2,1]

Output: 1'''


#code link:https://leetcode.com/problems/single-number/description/




class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        c=0
        for i in nums:
            if nums.count(i)==1:
                c=i

                        
        return c
