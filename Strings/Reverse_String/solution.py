"""
PYTHON SOLUTION - Reverse String
12/29/2025 12:50 AM
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## REVERSE STRING ##
    ####################
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Single character doesn't need reversal
        if len(s) <= 1:
            return
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Two pointers approach
        # Start: left at beginning, right at end
        # Swap elements and move pointers toward center
        # Stop when pointers meet or cross
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Swap characters at left and right
            s[left], s[right] = s[right], s[left]
            
            # Move pointers toward center
            left += 1
            right -= 1

#########
## EOF ##
#########