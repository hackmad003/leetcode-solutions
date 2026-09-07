"""
PYTHON SOLUTION - House Robber
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## ROB            ##
    ####################
    def rob(self, nums: List[int]) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Single house: just take everything from it (no adjacency conflict)
        if len(nums) == 1:
            return nums[0]
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Dynamic Programming
        # KEY INSIGHT: At each house, you have exactly two choices:
        #   (a) SKIP this house -> best total is whatever you had up through
        #       the PREVIOUS house
        #   (b) ROB this house -> best total is this house's money PLUS
        #       whatever you had up through the house BEFORE the previous one
        #       (since you can't rob two adjacent houses)
        # Take whichever choice gives the larger total.
        #
        # Track only the last two "best totals" instead of a full DP array,
        # achieving O(1) space.
        
        # prev2 = best total considering houses up to i-2
        # prev1 = best total considering houses up to i-1
        prev2 = 0
        prev1 = 0
        
        for money in nums:
            # Option (a): skip current house -> keep prev1
            # Option (b): rob current house -> money + prev2
            current = max(prev1, prev2 + money)
            
            # Slide the window forward for the next iteration
            prev2 = prev1
            prev1 = current
        
        return prev1

#########
## EOF ##
#########