"""
PYTHON SOLUTION - Shuffle an Array
08/11/2026
TIME COMPLEXITY: O(N) for both reset() and shuffle()
SPACE COMPLEXITY: O(N)
"""
import random
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## INIT           ##
    ####################
    def __init__(self, nums: List[int]):
        
        ####################
        ## MAIN SETUP     ##
        ####################
        # Keep the ORIGINAL array safe for reset() calls
        # Use a COPY for the "current" working array that gets shuffled
        self.original = nums[:]   # Snapshot of the original configuration
        self.array = nums[:]      # Working copy that reset()/shuffle() operate on
    
    
    ####################
    ## RESET          ##
    ####################
    def reset(self) -> List[int]:
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Restore the working array back to the original configuration
        # Use slicing to COPY values, not just reassign the reference
        self.array = self.original[:]
        
        return self.array
    
    
    ####################
    ## SHUFFLE        ##
    ####################
    def shuffle(self) -> List[int]:
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Fisher-Yates Shuffle Algorithm
        # Guarantees a UNIFORM random permutation (every arrangement equally likely)
        #
        # For each position i (from the end backward), pick a RANDOM index j
        # from the remaining unshuffled portion (0 to i, inclusive),
        # then swap the elements at i and j.
        # This "locks in" position i with a fairly-chosen element,
        # and shrinks the remaining "unshuffled" portion by one each time.
        
        n = len(self.array)
        
        # Iterate from the last index down to the first
        for i in range(n - 1, 0, -1):
            # Pick a random index from 0 to i (inclusive)
            j = random.randint(0, i)
            
            # Swap current element with the randomly chosen one
            self.array[i], self.array[j] = self.array[j], self.array[i]
        
        return self.array

#########
## EOF ##
#########

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()