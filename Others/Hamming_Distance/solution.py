"""
PYTHON SOLUTION - Hamming Distance
08/11/2026
TIME COMPLEXITY: O(K) where K = number of set bits in (x XOR y)
SPACE COMPLEXITY: O(1)
"""

##############
## SOLUTION ##
##############
class Solution:
    
    ######################
    ## HAMMING DISTANCE ##
    ######################
    def hammingDistance(self, x: int, y: int) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # If x and y are identical, there are no differing bits
        if x == y:
            return 0
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: XOR + Brian Kernighan's Bit Trick
        # KEY INSIGHT: XOR-ing two numbers produces a 1 in EVERY position
        # where the two numbers' bits DIFFER, and a 0 where they're the SAME.
        #   x = 0001
        #   y = 0100
        #   x^y = 0101  <- exactly marks the differing positions!
        #
        # So the Hamming distance is simply: "how many set bits are in (x XOR y)?"
        # We reuse the same Brian Kernighan's trick from the previous problem
        # to count those set bits efficiently.
        
        xor_result = x ^ y
        
        count = 0
        while xor_result != 0:
            xor_result = xor_result & (xor_result - 1)  # Clears lowest set bit
            count += 1
        
        return count

#########
## EOF ##
#########