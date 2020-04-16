***

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

***

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
            
            left_product=[0 for x in nums]
            result=[0 for x in nums ]
            product=1
            for i in range(len(nums)):
                
                if i>0:
                    product=nums[i-1]*product
                    left_product[i]=product
                else:
                    left_product[i]=1
                    
            product=1
            
            for i in reversed(range(len(nums))):
                
                if i< len(nums)-1:
                    product=nums[i+1]*product
                    result[i]=product*left_product[i]
                else:
                    result[i]=1*left_product[i]
            
            return result
