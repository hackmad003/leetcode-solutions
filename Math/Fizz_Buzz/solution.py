"""
PYTHON SOLUTION - Fizz Buzz
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1) extra (excluding the output array itself)
"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## FIZZ BUZZ      ##
    ####################
    def fizzBuzz(self, n: int) -> List[str]:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # n=0 isn't possible per constraints (1 <= n), so no special handling needed
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Single pass from 1 to n
        # For each number, check divisibility rules IN THE CORRECT ORDER:
        #   1. Check "divisible by BOTH 3 and 5" FIRST (most specific rule)
        #   2. Then check "divisible by 3 only"
        #   3. Then check "divisible by 5 only"
        #   4. Otherwise, just use the number itself as a string
        #
        # Order matters! If you checked "divisible by 3" before checking
        # "divisible by 3 AND 5", numbers like 15 would incorrectly get "Fizz"
        # instead of "FizzBuzz".
        
        answer = []
        
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        
        return answer

#########
## EOF ##
#########