"""
PYTHON SOLUTION - Reverse Linked List
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1) iterative / O(N) recursive
"""
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

##############
## SOLUTION ##
##############
class Solution:
    
    ##########################
    ## REVERSE LIST (ITER)  ##
    ##########################
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Empty list or single node is already "reversed"
        if not head or not head.next:
            return head
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Iterative pointer reversal
        # Walk through the list one node at a time
        # For each node, flip its 'next' pointer to point backward
        # Track 'prev' (the new reversed portion) and 'curr' (unprocessed portion)
        
        prev = None
        curr = head
        
        while curr:
            # Save the next node before we overwrite curr.next
            next_temp = curr.next
            
            # Reverse the pointer: curr now points backward to prev
            curr.next = prev
            
            # Move prev and curr both one step forward
            prev = curr
            curr = next_temp
        
        # 'prev' is now the new head of the reversed list
        return prev
    
    
    ##############################
    ## REVERSE LIST (RECURSIVE) ##
    ##############################
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Base case: empty list or single node is already "reversed"
        if not head or not head.next:
            return head
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Recursive reversal
        # Recurse all the way to the last node (this becomes new head)
        # As recursion unwinds, flip each pointer along the way
        
        # Recurse to the end of the list first
        new_head = self.reverseListRecursive(head.next)
        
        # Reverse the link: the next node should now point back to current
        head.next.next = head
        
        # Break the old forward link (prevents cycle)
        head.next = None
        
        # New head bubbles up unchanged through every recursive call
        return new_head

#########
## EOF ##
#########