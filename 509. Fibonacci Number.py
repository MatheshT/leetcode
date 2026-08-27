'''509. Fibonacci Number


Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.'''

#code link:https://leetcode.com/problems/fibonacci-number/description/


 def fib(self, n: int) -> int:
        f=0
        b=1
        for i in range(1,n+1):
            
            f,b=b,f+b
        return f
            
