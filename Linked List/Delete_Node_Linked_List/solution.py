"""
PYTHON SOLUTION - Delete Node in a Linked List
08/11/2026
TIME COMPLEXITY: O(1)
SPACE COMPLEXITY: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## DELETE NODE    ##
    ####################
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Guaranteed: node is not the tail and has a valid next node,
        # so no special edge case handling is needed here.
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Since we don't have access to the previous node,
        # we can't unlink 'node' the traditional way (prev.next = node.next).
        # Instead, we "become" the next node:
        #   1. Copy the next node's value into the current node
        #   2. Skip over the next node by relinking node.next
        # This effectively deletes what WAS the current node's identity,
        # while keeping the list's values and order correct.
        
        # Step 1: Overwrite current node's value with the next node's value
        node.val = node.next.val
        
        # Step 2: Bypass the next node (which is now a duplicate)
        node.next = node.next.next

#########
## EOF ##
#########