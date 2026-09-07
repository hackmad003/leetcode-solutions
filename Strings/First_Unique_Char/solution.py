"""
PYTHON SOLUTION - First Unique Character in a String
12/29/2025 01:10 AM
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
"""

##############
## SOLUTION ##
##############
class Solution:
    
    #################################
    ## FIRST UNIQUE CHARACTER      ##
    #################################
    def firstUniqChar(self, s: str) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Single character is always unique
        if len(s) == 1:
            return 0
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Two-pass approach with hash map
        # Pass 1: Count frequency of each character
        # Pass 2: Find first character with frequency 1
        
        # PASS 1: Count character frequencies
        char_count = {}
        
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # PASS 2: Find first character with count = 1
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        
        # No unique character found
        return -1

#########
## EOF ##
#########