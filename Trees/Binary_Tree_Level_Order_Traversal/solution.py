"""
PYTHON SOLUTION - Binary Tree Level Order Traversal
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(N)
"""
from typing import List, Optional
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
    ## LEVEL ORDER          ##
    ##########################
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Empty tree has no levels to traverse
        if not root:
            return []
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Breadth-First Search (BFS) using a queue
        # Process the tree one LEVEL at a time
        # For each level:
        #   1. Record how many nodes are currently in the queue (= size of this level)
        #   2. Pop exactly that many nodes, collecting their values
        #   3. Push their children (next level) onto the queue
        # Repeat until the queue is empty
        
        result = []
        queue = deque([root])
        
        while queue:
            # Number of nodes at the CURRENT level
            level_size = len(queue)
            current_level = []
            
            # Process exactly 'level_size' nodes (this level only)
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Enqueue children for the NEXT level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add this completed level to the result
            result.append(current_level)
        
        return result

#########
## EOF ##
#########