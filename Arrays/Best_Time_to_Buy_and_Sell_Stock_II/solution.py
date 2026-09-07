"""
PYTHON SOLUTION - Best Time to Buy and Sell Stock II
12/25/2025 10:50 PM
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
Note: Python and Python3 use the same code

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.
Find and return the maximum profit you can achieve.

"""

##############
## SOLUTION ##
##############
class Solution:
    
    ################
    ## MAX PROFIT ##
    ################
    def maxProfit(self, prices: list[int]) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # If array has only one element or is empty, no profit can be made
        if len(prices) <= 1:
            return 0
        
        # Variable to track total profit
        profit = 0
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Capture every upward price movement
        # If tomorrow's price > today's price, buy today and sell tomorrow
        for i in range(1, len(prices)):
            # If price increased, add the profit
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        
        return profit

#########
## EOF ##
#########
