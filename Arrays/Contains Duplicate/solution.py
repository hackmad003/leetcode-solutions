"""
PYTHON SOLUTION - Contains Duplicate
12/28/2025 11:20 PM
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""

##############
## SOLUTION ##
##############
class Solution:
    
    #######################
    ## CONTAINS DUPLICATE ##
    #######################
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # If array has only one element, no duplicates possible
        if len(nums) <= 1:
            return False
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Use set to track seen elements
        # If we encounter an element already in set, we found a duplicate
        
        seen = set()
        
        for num in nums:
            # If element already exists in set, duplicate found
            if num in seen:
                return True
            # Add element to set
            seen.add(num)
        
        # No duplicates found
        return False

#########
## EOF ##
#########