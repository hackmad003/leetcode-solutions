"""
PYTHON SOLUTION - Pascal's Triangle
08/11/2026
TIME COMPLEXITY: O(numRows^2)
SPACE COMPLEXITY: O(1) extra (excluding the output itself)
"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## GENERATE       ##
    ####################
    def generate(self, numRows: int) -> List[List[int]]:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # A single row is just [1] - the base case of the triangle
        if numRows == 1:
            return [[1]]
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Build row by row, using the PREVIOUS row to compute
        # the CURRENT row.
        # KEY INSIGHT: Every row starts and ends with 1. Every value in
        # between is the SUM of the two values directly above it in the
        # previous row (at positions j-1 and j).
        #
        # Example: previous row = [1,3,3,1]
        #          new row starts as [1, ?, ?, ?, 1]
        #          middle values: prev[0]+prev[1]=1+3=4, prev[1]+prev[2]=3+3=6,
        #                         prev[2]+prev[3]=3+1=4
        #          new row = [1,4,6,4,1]
        
        triangle = [[1]]  # First row is always just [1]
        
        for row_num in range(1, numRows):
            previous_row = triangle[row_num - 1]
            
            # Every row starts with 1
            new_row = [1]
            
            # Fill in the middle values using the sum of adjacent
            # elements from the previous row
            for j in range(1, row_num):
                new_row.append(previous_row[j - 1] + previous_row[j])
            
            # Every row (except the very first) ends with 1
            new_row.append(1)
            
            triangle.append(new_row)
        
        return triangle

#########
## EOF ##
#########