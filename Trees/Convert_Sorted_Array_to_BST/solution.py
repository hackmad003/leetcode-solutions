"""
PYTHON SOLUTION - Convert Sorted Array to Binary Search Tree
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(log N)
"""
from typing import List, Optional

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
    
    ##################################
    ## SORTED ARRAY TO BST          ##
    ##################################
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Empty array means no tree to build
        if not nums:
            return None
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Recursive divide-and-conquer using the MIDDLE element as root
        # Since the array is sorted, picking the middle element as root guarantees:
        #   - All elements to its left are smaller -> become the left subtree
        #   - All elements to its right are larger -> become the right subtree
        # Recursively repeat this for each half, which naturally balances the tree
        # (each subtree splits its range roughly in half every time)
        
        return self.build(nums, 0, len(nums) - 1)
    
    
    def build(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        """Helper function: recursively builds a balanced BST from nums[left..right]."""
        
        # Base case: no elements left in this range
        if left > right:
            return None
        
        # Choose the middle index as root (use left-middle for even-length ranges,
        # which naturally matches one of the accepted balanced outputs)
        mid = (left + right) // 2
        
        # Create the root node with the middle value
        root = TreeNode(nums[mid])
        
        # Recursively build left subtree from the left half
        root.left = self.build(nums, left, mid - 1)
        
        # Recursively build right subtree from the right half
        root.right = self.build(nums, mid + 1, right)
        
        return root

#########
## EOF ##
#########