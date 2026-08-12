'''412. Fizz Buzz

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]'''



#code link:https://leetcode.com/problems/fizz-buzz/description/






class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        b=[]
        for i in range(1,n+1):

            if i%3==0 and i%5==0:
                b.append("FizzBuzz")
            elif i%3==0:
                b.append("Fizz")
            elif i%5==0:
                b.append("Buzz")
            else:
                b.append(str(i))
        return b
