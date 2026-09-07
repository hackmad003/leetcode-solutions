"""
PYTHON SOLUTION - Valid Anagram
12/29/2025 01:20 AM
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
"""

"""

{}   # Dictionary (hash map) - key-value pairs
[]   # List (array) - ordered elements

The dict is used to count character frequencies!

char_count = {}

# For string s: ADD to count
for char in "anagram":
    char_count[char] = char_count.get(char, 0) + 1
# Result: {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}

# For string t: SUBTRACT from count
for char in "nagaram":
    char_count[char] = char_count.get(char, 0) - 1
# Result: {'a': 0, 'n': 0, 'g': 0, 'r': 0, 'm': 0}

# If all values are 0 → Anagram! ✓
# If all values equal each other → Anagram! ✓

"""


##############
## SOLUTION ##
##############
class Solution:
    
    ###################
    ## VALID ANAGRAM ##
    ###################
    def isAnagram(self, s: str, t: str) -> bool:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # If lengths differ, cannot be anagram
        if len(s) != len(t):
            return False
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Count character frequencies in both strings
        # If frequency maps are identical, strings are anagrams
        
        # Count character frequencies in s
        char_count_s = {}
        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1
        
        # Count character frequencies in t
        char_count_t = {}
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1
        
        # Compare frequency maps
        return char_count_s == char_count_t

#########
## EOF ##
#########