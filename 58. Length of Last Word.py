'''58. Length of Last Word


Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.'''


#code link:https://leetcode.com/problems/length-of-last-word/description/



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    
        c=s.split()
        return len(c[-1])
