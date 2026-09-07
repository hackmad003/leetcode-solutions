"""
PYTHON SOLUTION - Best Time to Buy and Sell Stock
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## MAX PROFIT     ##
    ####################
    def maxProfit(self, prices: List[int]) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Fewer than 2 prices means no valid buy/sell pair exists
        if len(prices) < 2:
            return 0
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Single pass, tracking the minimum price seen so far
        # For each day, ask: "If I sold TODAY, having bought at the LOWEST
        # price seen so far, what would my profit be?"
        # Keep track of the best (maximum) profit found across all days.
        #
        # This works because we only need to know the BEST buy point
        # BEFORE each potential sell point - no need to check all pairs.
        
        min_price = prices[0]   # Lowest price seen so far
        max_profit = 0          # Best profit found so far
        
        for price in prices[1:]:
            # Option 1: Sell today at current price (using best buy so far)
            profit_if_sold_today = price - min_price
            max_profit = max(max_profit, profit_if_sold_today)
            
            # Option 2: Update minimum price if today's price is even lower
            min_price = min(min_price, price)
        
        return max_profit

#########
## EOF ##
#########