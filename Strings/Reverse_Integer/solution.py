"""
PYTHON SOLUTION - Reverse Integer
12/29/2025 01:00 AM
TIME COMPLEXITY: O(log N)
SPACE COMPLEXITY: O(1)
"""

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## REVERSE INTEGER ##
    ####################
    def reverse(self, x: int) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # If x is 0, return 0
        if x == 0:
            return 0
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Extract digits and build reversed number
        # 1. Handle sign separately
        # 2. Reverse digits by extracting one at a time
        # 3. Check for overflow before returning
        
        # Define 32-bit signed integer bounds
        INT_MIN = -2**31  # -2,147,483,648
        INT_MAX = 2**31 - 1  # 2,147,483,647
        
        # Handle negative numbers
        sign = 1 if x > 0 else -1 # Save the Sign
        x = abs(x) # Take Absolute Value
        
        # Reverse the digits
        reversed_num = 0
        
        while x != 0:
            # Extract last digit
            digit = x % 10
            
            # Check for overflow BEFORE adding the digit
            # If reversed_num > INT_MAX // 10, then reversed_num * 10 will overflow
            # If reversed_num == INT_MAX // 10 and digit > 7, it will overflow
            if reversed_num > INT_MAX // 10 or (reversed_num == INT_MAX // 10 and digit > 7):
                return 0
            
            # Build reversed number
            reversed_num = reversed_num * 10 + digit
            
            # Remove last digit from x
            x //= 10
        
        # Apply sign and check bounds
        result = sign * reversed_num
        
        # Final overflow check
        if result < INT_MIN or result > INT_MAX:
            return 0
        
        return result

#########
## EOF ##
#########