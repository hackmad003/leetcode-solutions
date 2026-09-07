"""
PYTHON SOLUTION - Two Sum
12/29/2025 12:20 AM
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ############
    ## TWO SUM ##
    ############
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Problem guarantees exactly one solution and at least 2 elements
        # No explicit edge case handling needed
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Use hash map to store seen numbers and their indices
        # For each number, check if complement (target - num) exists in map
        # If yes, return indices. If no, add current number to map.
        
        # Hash map: {number: index}
        seen = {}
        
        for i, num in enumerate(nums):
            # Calculate complement needed to reach target
            complement = target - num
            
            # Check if complement exists in our map
            if complement in seen:
                # Found it! Return indices
                return [seen[complement], i]
            
            # Haven't found pair yet, store current number and index
            seen[num] = i
        
        # Problem guarantees exactly one solution, so we'll never reach here
        return []

#########
## EOF ##
#########