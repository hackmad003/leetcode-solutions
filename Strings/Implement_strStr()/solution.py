"""
PYTHON SOLUTION - Find the Index of the First Occurrence in a String
08/11/2026
TIME COMPLEXITY: O(N * M)
SPACE COMPLEXITY: O(1)
"""

##############
## SOLUTION ##
##############
class Solution:
    
    ##############
    ## STR STR  ##
    ##############
    def strStr(self, haystack: str, needle: str) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Needle longer than haystack can never be found
        n = len(haystack)
        m = len(needle)
        
        if m > n:
            return -1
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Sliding window with brute force comparison
        # Try every possible starting position in haystack
        # At each position, check if needle matches the substring
        # Return the first index where it matches, else -1
        
        # Only need to check starting positions where needle could still fit
        for i in range(n - m + 1):
            
            # Assume match until proven otherwise
            match = True
            
            # Compare needle against haystack starting at position i
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            
            # If all characters matched, return starting index
            if match:
                return i
        
        # No match found anywhere
        return -1

#########
## EOF ##
#########