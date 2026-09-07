"""
PYTHON SOLUTION - Valid Sudoku
12/29/2025 12:30 AM
TIME COMPLEXITY: O(1) - technically O(81) = O(1) since board is fixed 9x9
SPACE COMPLEXITY: O(1) - technically O(81) = O(1) since board is fixed 9x9
"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ##################
    ## VALID SUDOKU ##
    ##################
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Board is guaranteed to be 9x9, no edge case handling needed
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Use sets to track seen numbers in rows, columns, and boxes
        # For each cell, check if number already exists in:
        # 1. Its row
        # 2. Its column
        # 3. Its 3x3 box
        # If any duplicate found, return False
        # Otherwise, return True
        
        # Create sets for each row, column, and 3x3 box
        rows = [set() for _ in range(9)]      # 9 row sets
        cols = [set() for _ in range(9)]      # 9 column sets
        boxes = [set() for _ in range(9)]     # 9 box sets
        
        # Iterate through each cell in the board
        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                
                # Skip empty cells
                if cell == '.':
                    continue
                
                # Calculate which 3x3 box this cell belongs to
                box_index = (r // 3) * 3 + (c // 3)
                
                # Check if number already exists in row, column, or box
                if cell in rows[r] or cell in cols[c] or cell in boxes[box_index]:
                    return False
                
                # Add number to respective sets
                rows[r].add(cell)
                cols[c].add(cell)
                boxes[box_index].add(cell)
        
        # If no duplicates found, board is valid
        return True

#########
## EOF ##
#########