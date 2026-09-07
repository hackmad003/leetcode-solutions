"""
PYTHON SOLUTION - Symmetric Tree
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(H) recursive / O(N) iterative (worst case, wide tree)
"""
from typing import Optional
from collections import deque

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
    ## SYMMETRIC (RECURSIVE) #
    ##########################
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Empty tree is trivially symmetric
        if not root:
            return True
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: A tree is symmetric if its left and right subtrees
        # are MIRROR IMAGES of each other.
        # Compare left/right subtrees as a pair, checking:
        #   1. Both nodes are None (symmetric so far) OR
        #   2. Both nodes exist, values match, AND
        #      left.left mirrors right.right, left.right mirrors right.left
        
        return self.isMirror(root.left, root.right)
        #return self.isSymmetricIterative(root)

    
    
    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        """Helper function: checks if two subtrees are mirror images of each other."""
        
        # Both None: symmetric at this branch
        if not left and not right:
            return True
        
        # Only one is None (the other isn't): NOT symmetric
        if not left or not right:
            return False
        
        # Both exist: values must match, AND their cross-children must mirror
        return (left.val == right.val and
                self.isMirror(left.left, right.right) and
                self.isMirror(left.right, right.left))
    
    
    ##########################
    ## SYMMETRIC (ITERATIVE) #
    ##########################
    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        
        ####################
        ## EDGE CASE      ##
        ####################
        if not root:
            return True
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Use a queue to process node pairs level by level
        # Push pairs of nodes that SHOULD mirror each other
        # Pop pairs, verify they match, then push their children
        # (in mirrored order: outer-outer, inner-inner)
        
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            
            # Both None: this pair is symmetric, continue checking others
            if not left and not right:
                continue
            
            # Only one None: NOT symmetric
            if not left or not right:
                return False
            
            # Values must match
            if left.val != right.val:
                return False
            
            # Push children in mirrored order:
            # left.left pairs with right.right (outer edges)
            # left.right pairs with right.left (inner edges)
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        
        return True

#########
## EOF ##
#########