"""
PYTHON SOLUTION - Validate Binary Search Tree
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
    
    ##########################
    ## VALID BST            ##
    ##########################
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # An empty tree is trivially a valid BST
        if not root:
            return True
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Recursive DFS with valid range tracking
        # A common mistake is only checking node.val vs its immediate children.
        # Instead, each node must satisfy a valid (low, high) RANGE inherited
        # from ALL its ancestors, not just its direct parent.
        #
        # Start with the widest possible range (-infinity, +infinity)
        # As we recurse left, the upper bound tightens to the parent's value
        # As we recurse right, the lower bound tightens to the parent's value
        
        return self.validate(root, float('-inf'), float('inf'))
    
    
    def validate(self, node: Optional[TreeNode], low: float, high: float) -> bool:
        """Helper function: checks if node's value falls within (low, high),
        and recursively validates left/right subtrees with updated bounds."""
        
        # Base case: an empty subtree is always valid
        if not node:
            return True
        
        # Current node's value must be strictly within the allowed range
        if node.val <= low or node.val >= high:
            return False
        
        # Recurse left: upper bound becomes current node's value
        # Recurse right: lower bound becomes current node's value
        return (self.validate(node.left, low, node.val) and
                self.validate(node.right, node.val, high))

#########
## EOF ##
#########