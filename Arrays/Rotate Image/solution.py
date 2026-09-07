"""
PYTHON SOLUTION - Rotate Image
12/29/2025 12:40 AM
TIME COMPLEXITY: O(N²)
SPACE COMPLEXITY: O(1)
"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ################
    ## ROTATE IMG ##
    ################
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Single element matrix doesn't need rotation
        if len(matrix) <= 1:
            return
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Rotate 90° clockwise = Transpose + Reverse each row
        # Step 1: Transpose matrix (swap rows and columns)
        # Step 2: Reverse each row
        
        n = len(matrix)
        
        # STEP 1: Transpose the matrix
        # Swap matrix[i][j] with matrix[j][i]
        for i in range(n):
            for j in range(i + 1, n):  # Start from i+1 to avoid swapping twice
                # Swap elements across diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # STEP 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()  # Or: matrix[i] = matrix[i][::-1]

#########
## EOF ##
#########