"""
PYTHON SOLUTION - Number of 1 Bits (Optimized for MANY repeated calls)
08/11/2026
TIME COMPLEXITY: O(1) per call after O(2^16) one-time precomputation
SPACE COMPLEXITY: O(2^16) for the precomputed lookup table
"""

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## INIT           ##
    ####################
    def __init__(self):
        
        ####################
        ## PRECOMPUTATION ##
        ####################
        # Strategy: Precompute Hamming weights for ALL 16-bit numbers ONCE
        # Then, for any 32-bit number, split it into two 16-bit halves,
        # look up each half's weight, and add them together.
        #
        # This is a "divide and conquer with caching" approach - since
        # 32-bit numbers can be split as: (high 16 bits) + (low 16 bits)
        # popcount(n) = popcount(high_half) + popcount(low_half)
        
        self.table_size = 1 << 16  # 65,536 possible 16-bit values
        self.bit_counts = [0] * self.table_size
        
        # Build the lookup table using Brian Kernighan's trick ONCE
        for i in range(1, self.table_size):
            # Each value's count = count of (i with lowest bit removed) + 1
            # This reuses PREVIOUSLY computed values in the same table!
            self.bit_counts[i] = self.bit_counts[i & (i - 1)] + 1
    
    
    ######################
    ## HAMMING WEIGHT   ##
    ######################
    def hammingWeight(self, n: int) -> int:
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Split n into its lower 16 bits and upper 16 bits
        # Look up each half's precomputed weight, then sum them
        
        lower_half = n & 0xFFFF          # Extract lowest 16 bits
        upper_half = (n >> 16) & 0xFFFF  # Extract next 16 bits
        
        return self.bit_counts[lower_half] + self.bit_counts[upper_half]

#########
## EOF ##
#########





"""
PYTHON SOLUTION - Number of 1 Bits (Hamming Weight)
08/11/2026
TIME COMPLEXITY: O(K) where K = number of set bits (Brian Kernighan's trick)
SPACE COMPLEXITY: O(1)
"""

##############
## SOLUTION ##
##############
class Solution:
    
    ######################
    ## HAMMING WEIGHT   ##
    ######################
    def hammingWeight(self, n: int) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # n=0 would have zero set bits (though constraints say n >= 1)
        if n == 0:
            return 0
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Brian Kernighan's Bit Trick
        # KEY INSIGHT: The operation (n & (n-1)) always CLEARS the
        # LOWEST set bit of n, without affecting any other bits.
        #
        # Why this works:
        #   - Subtracting 1 flips all bits from the lowest set bit
        #     rightward (that bit becomes 0, everything after becomes 1)
        #   - ANDing with the original n then cancels out that entire
        #     "flipped" region, effectively removing just the lowest 1-bit
        #
        # By repeating this until n becomes 0, we count exactly how many
        # set bits existed - and we only loop ONCE PER SET BIT, not once
        # per total bit position (making this faster than checking all 32 bits
        # when n has few set bits).
        
        count = 0
        
        while n != 0:
            n = n & (n - 1)  # Clears the lowest set bit
            count += 1
        
        return count

#########
## EOF ##
#########