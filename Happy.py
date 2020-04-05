"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


"""

class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        #Steps can be identify the number of digits in 'n'
        #Break the integer and find the sum. 
        # Calcualte the square of the number.
        # Include the number in the list if not present 
        list=[]
        
        
        
        def  sqrsum(n):
            
                result=0 
                
                while n > 0:
                    rem = n % 10
                    result = result + rem*rem
                    n = n//10


                return result


        while sqrsum(n) not in list:
            num1= sqrsum(n)
            if num1==1:
                return True
            else:
                list.append(num1)
                n=num1
        
        return False
            

            
        
        
            
