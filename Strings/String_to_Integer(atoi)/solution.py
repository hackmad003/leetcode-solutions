"""
PYTHON SOLUTION - String to Integer (atoi)
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
"""

##############
## SOLUTION ##
##############
class Solution:
    
    ##############
    ## MY ATOI  ##
    ##############
    def myAtoi(self, s: str) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Empty string has no digits to convert
        if not s:
            return 0
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Single pass with an index pointer
        # 1. Skip leading whitespace
        # 2. Check for sign (+/-)
        # 3. Read digits, building the number
        # 4. Clamp to 32-bit signed integer range
        
        INT_MIN = -2**31   # -2,147,483,648
        INT_MAX = 2**31 - 1  # 2,147,483,647
        
        n = len(s)
        i = 0
        
        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        if i == n:
            return 0
        
        # Determine sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Read digits and build number
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            
            # Early clamp check to avoid unbounded number buildup
            if num > INT_MAX:
                return INT_MAX if sign == 1 else INT_MIN
            
            i += 1
        
        # Apply sign
        result = sign * num
        
        return result

#########
## EOF ##
#########