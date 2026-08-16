'''268. Missing Number


Input: nums = [3,0,1]

Output: 2

Explanation:

n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.'''

#code link:https://leetcode.com/problems/missing-number/description/


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        c=sorted(nums)
        d=0
        for i in range(len(c)+1):
            if i not in c:
                d=i
        return d
