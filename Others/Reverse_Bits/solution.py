"""
PYTHON SOLUTION - Reverse Bits
08/11/2026
TIME COMPLEXITY: O(32) = O(1) (fixed 32-bit width)
SPACE COMPLEXITY: O(1)
"""

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## REVERSE BITS   ##
    ####################
    def reverseBits(self, n: int) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # n=0 reversed is still 0 (all 32 bits are zero either way)
        if n == 0:
            return 0
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Bit-by-bit extraction and reconstruction
        # KEY INSIGHT: To reverse a 32-bit number, process it exactly like
        # reversing a string of digits - peel off bits from ONE END and
        # append them to the OTHER END of the result.
        #
        # For each of the 32 bit positions:
        #   1. Extract the LOWEST bit of n (using n & 1)
        #   2. Shift the result LEFT by 1 (make room for the new bit)
        #   3. Place the extracted bit into that new rightmost slot
        #   4. Shift n RIGHT by 1 (move to the next bit to process)
        
        result = 0
        
        for _ in range(32):
            # Make room in result for the next bit (shift existing bits left)
            result = result << 1
            
            # Extract the lowest bit of n and place it into result
            result = result | (n & 1)
            
            # Move to the next bit of n
            n = n >> 1
        
        return result

#########
## EOF ##
#########




"""
PYTHON SOLUTION - Reverse Bits (Optimized for MANY repeated calls)
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
        # Strategy: Precompute the BIT-REVERSAL of every possible 16-bit
        # value ONCE. Then, for any 32-bit number, split it into two
        # 16-bit halves, reverse each half using the lookup table, and
        # SWAP their positions (since reversing the whole number also
        # flips which half ends up on which side).
        #
        # Example: reversing 32 bits [HIGH 16][LOW 16]
        #   -> becomes [reverse(LOW 16)][reverse(HIGH 16)]
        
        self.table_size = 1 << 16  # 65,536 possible 16-bit values
        self.reverse_table = [0] * self.table_size
        
        # Build the lookup table using the same bit-by-bit method,
        # but only for 16 bits instead of 32
        for num in range(self.table_size):
            reversed_val = 0
            temp = num
            for _ in range(16):
                reversed_val = (reversed_val << 1) | (temp & 1)
                temp = temp >> 1
            self.reverse_table[num] = reversed_val
    
    
    ####################
    ## REVERSE BITS   ##
    ####################
    def reverseBits(self, n: int) -> int:
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Split n into its lower 16 bits and upper 16 bits
        lower_half = n & 0xFFFF          # Extract lowest 16 bits
        upper_half = (n >> 16) & 0xFFFF  # Extract next 16 bits
        
        # Reverse each half using the precomputed table,
        # then SWAP their positions in the final result:
        #   reversed(lower_half) goes to the HIGH position
        #   reversed(upper_half) goes to the LOW position
        return (self.reverse_table[lower_half] << 16) | self.reverse_table[upper_half]

#########
## EOF ##
#########