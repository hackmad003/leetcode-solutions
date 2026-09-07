"""
PYTHON SOLUTION - Maximum Depth of Binary Tree
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(H)
"""
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

##############
## SOLUTION ##
##############
class Solution:
    
    ######################
    ## MAX DEPTH        ##
    ######################
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # An empty tree has depth 0
        if not root:
            return 0
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Recursive Depth-First Search (DFS)
        # The depth of a tree = 1 (for current node) + depth of its deeper subtree
        # Recursively compute the depth of the left and right subtrees,
        # take the max of the two, and add 1 for the current node
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)

#########
## EOF ##
#########