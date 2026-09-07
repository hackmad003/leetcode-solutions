"""
PYTHON SOLUTION - Single Number
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## SINGLE NUMBER  ##
    ####################
    def singleNumber(self, nums: List[int]) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Single element array is the answer itself
        if len(nums) == 1:
            return nums[0]
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: XOR all elements together
        # XOR properties:
        #   a ^ a = 0  (number XOR itself = 0)
        #   a ^ 0 = a  (number XOR 0 = itself)
        # All duplicate pairs cancel out to 0
        # Only the single number remains!
        
        result = 0
        
        for num in nums:
            result ^= num
        
        return result

#########
## EOF ##
#########