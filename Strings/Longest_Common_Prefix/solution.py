"""
PYTHON SOLUTION - Longest Common Prefix
08/11/2026
TIME COMPLEXITY: O(N * M)
SPACE COMPLEXITY: O(1)
"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    #############################
    ## LONGEST COMMON PREFIX   ##
    #############################
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Empty list or list containing an empty string means no common prefix
        if not strs:
            return ""
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Vertical scanning
        # Use the first string as a reference
        # Compare character-by-character (column by column) against all other strings
        # Stop as soon as a mismatch is found or a string runs out of characters
        
        # Use first string as the initial candidate prefix
        first_word = strs[0]
        
        # Iterate through each character position in the first word
        for i, char in enumerate(first_word):
            
            # Compare this character against the same position in every other string
            for word in strs[1:]:
                
                # If this word is too short, or characters don't match, stop here
                if i == len(word) or word[i] != char:
                    return first_word[:i]
        
        # If we never broke out, the entire first word is the common prefix
        return first_word

#########
## EOF ##
#########