"""
PYTHON SOLUTION - Climbing Stairs
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
"""

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## CLIMB STAIRS   ##
    ####################
    def climbStairs(self, n: int) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # 1 step or fewer: only one way to climb (just take that single step)
        if n <= 2:
            return n
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Dynamic Programming (Fibonacci pattern)
        # KEY INSIGHT: To reach step n, your LAST move was either:
        #   - A 1-step move from step (n-1), OR
        #   - A 2-step move from step (n-2)
        # So: ways(n) = ways(n-1) + ways(n-2)
        # This is exactly the Fibonacci sequence!
        #
        # Instead of storing the whole DP array (O(N) space), we only need
        # the last two values at any time, achieving O(1) space.
        
        # ways(1) = 1 (one way: single 1-step)
        # ways(2) = 2 (two ways: 1+1, or 2)
        prev2 = 1   # represents ways(i-2)
        prev1 = 2   # represents ways(i-1)
        
        # Build up from step 3 to step n
        for i in range(3, n + 1):
            current = prev1 + prev2
            
            # Slide the window forward for the next iteration
            prev2 = prev1
            prev1 = current
        
        return prev1

#########
## EOF ##
#########