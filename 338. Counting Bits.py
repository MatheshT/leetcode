'''338. Counting Bits



Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10'''


#code link:https://leetcode.com/problems/counting-bits/description/




class Solution:
    def countBits(self, n: int) -> List[int]:
        b=[0]*(n+1)
        for i in range(1,n+1):
           b[i]=b[i>>1] + (i&1)
        
        return b
