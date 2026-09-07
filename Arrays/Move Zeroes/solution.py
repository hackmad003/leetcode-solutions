"""
PYTHON SOLUTION - Move Zeroes
12/29/2025 12:10 AM
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ################
    ## MOVE ZEROES ##
    ################
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ####################
        ## EDGE CASE      ##
        ####################
        # If array has only one element, nothing to move
        if len(nums) <= 1:
            return
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Two pointers - optimal approach
        # left pointer: tracks position for next non-zero element
        # right pointer: iterates through array
        # When we find non-zero, swap with left pointer position
        
        left = 0  # Position for next non-zero element
        
        # Iterate through array
        for right in range(len(nums)):
            # If current element is non-zero
            if nums[right] != 0:
                # Swap with left pointer position
                nums[left], nums[right] = nums[right], nums[left]
                # Move left pointer forward
                left += 1
        
        # After loop, all non-zeros are at front, zeros at end
        # No need to explicitly fill zeros (they're already there from swaps)

#########
## EOF ##
#########