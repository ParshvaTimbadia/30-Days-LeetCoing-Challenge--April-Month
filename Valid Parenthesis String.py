***
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True

Note:
The string size will be in the range [1, 100].
***

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack1=[]
        stack2=[]
        
        if len(s)==0 or s=='*':
            return True
        
        elif len(s)==1:
            return False
        
        for i in range(len(s)):
            
            if s[i]=='(':
                stack1.append(i)
            elif s[i]==')':
                if len(stack1)==0 and len(stack2)==0:
                    return False
                if stack1:
                    stack1.pop()
                elif stack2: 
                    stack2.pop()
                else: 
                    return False
            else: 
                stack2.append(i)
        
        while stack1 and stack2:
            if stack1[-1] < stack2[-1]:
                stack1.pop()
                stack2.pop()
            else: 
                break
        
        return len(stack1)==0
        
        
