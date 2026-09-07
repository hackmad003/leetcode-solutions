"""
PYTHON SOLUTION - Roman to Integer
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
"""

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## ROMAN TO INT   ##
    ####################
    def romanToInt(self, s: str) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Empty string isn't possible per constraints (1 <= s.length)
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Single pass, comparing each symbol to the NEXT one
        # KEY INSIGHT: In standard left-to-right reading, if a symbol's value
        # is SMALLER than the value of the symbol immediately after it,
        # that symbol should be SUBTRACTED (this is the "IV", "IX", "XL", etc. case).
        # Otherwise, it should be ADDED normally.
        #
        # Example: "IV" -> I(1) is less than V(5), so subtract: -1 + 5 = 4
        #          "VI" -> V(5) is NOT less than I(1), so add both: 5 + 1 = 6
        
        # Map each Roman numeral symbol to its integer value
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            current_value = roman_values[s[i]]
            
            # Check if there's a NEXT character and if current < next
            # (this signals a "subtractive" pair like IV, IX, XL, etc.)
            if i + 1 < n and current_value < roman_values[s[i + 1]]:
                total -= current_value
            else:
                total += current_value
        
        return total

#########
## EOF ##
#########