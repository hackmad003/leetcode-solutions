"""
PYTHON SOLUTION - Power of Three
08/11/2026
TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
"""

##############
## SOLUTION ##
##############
class Solution:
    
    ##########################
    ## IS POWER OF THREE    ##
    ##########################
    def isPowerOfThree(self, n: int) -> bool:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Zero and negative numbers can never be a power of 3
        # (3^x is always positive for any integer x)
        if n <= 0:
            return False
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Mathematical trick using the LARGEST power of 3
        # that fits within a 32-bit signed integer (no loops/recursion needed!)
        #
        # KEY INSIGHT: 3 is a PRIME number. This means the only divisors
        # of 3^k are 1, 3, 9, 27, ..., 3^k itself - no other prime factors
        # can sneak in.
        #
        # Find the LARGEST power of 3 that fits in a 32-bit signed integer:
        #   3^19 = 1,162,261,467 (this fits within INT_MAX = 2,147,483,647)
        #   3^20 would exceed the 32-bit range
        #
        # If n IS a power of 3, then n must EVENLY DIVIDE this largest power,
        # since all powers of 3 are just this largest one divided by some
        # smaller power of 3 (3^19 = 3^k * 3^(19-k) for any valid k <= 19).
        # If n does NOT evenly divide 3^19, n cannot be a power of 3.
        
        MAX_POWER_OF_THREE = 1162261467  # This is 3^19
        
        return MAX_POWER_OF_THREE % n == 0

#########
## EOF ##
#########