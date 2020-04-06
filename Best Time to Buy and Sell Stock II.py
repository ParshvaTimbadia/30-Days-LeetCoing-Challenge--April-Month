***
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

***


# One Possible Solution mentioned in the multi-line comments:

***

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Two pointer method will do 
        
        start=0
        
        max_sum=0
        
        for end in range(1,len(prices)):
            
            if start==end:
                continue
            
            
            if prices[start] >= prices[end] :
                start+=1
                
                
            elif  end < len(prices)-1 and prices[end+1] > prices[end]  :
                continue
            
            else:
                
                max_sum = max_sum + prices[end]- prices[start]
                start=end+1
                
                
                
***

# That was my first attempt complexity was high so now I came up with a better solution:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_prof=0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                max_prof= max_prof+ prices[i]-prices[i-1]
                
        return max_prof    
        
        
