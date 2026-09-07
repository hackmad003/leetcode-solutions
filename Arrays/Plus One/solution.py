"""
PYTHON SOLUTION - Plus One
12/29/2025 12:00 AM
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1) - O(N) worst case

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ##############
    ## PLUS ONE ##
    ##############
    def plusOne(self, digits: List[int]) -> List[int]:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Single digit 9 becomes [1, 0]
        # This is handled by main algorithm
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Start from rightmost digit and handle carry
        # Add 1 to last digit, propagate carry left if needed
        
        n = len(digits)
        
        # Iterate from right to left
        for i in range(n - 1, -1, -1):
            # Add 1 to current digit
            digits[i] += 1
            
            # If no carry needed, we're done
            if digits[i] < 10:
                return digits
            
            # Carry needed: set current digit to 0 and continue
            digits[i] = 0
        
        # If we reach here, all digits were 9 (e.g., [9,9,9] -> [1,0,0,0])
        # Prepend 1 to array
        return [1] + digits

#########
## EOF ##
#########