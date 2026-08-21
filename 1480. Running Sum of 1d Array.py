'''1480. Running Sum of 1d Array




Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].'''



#code link:https://leetcode.com/problems/running-sum-of-1d-array/description/



class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        j=[]
        k=0
        for i in nums:
            
            k+=i
            j.append(k)
        return j
