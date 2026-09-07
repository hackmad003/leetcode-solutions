"""
PYTHON SOLUTION - Remove Nth Node From End of List
08/11/2026
TIME COMPLEXITY: O(L)
SPACE COMPLEXITY: O(1)
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
    
    ##############################
    ## REMOVE NTH FROM END      ##
    ##############################
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Use a dummy node before head to simplify removing the head itself
        # (e.g., when n == length of the list, we remove the very first node)
        dummy = ListNode(0)
        dummy.next = head
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Two pointers with a gap of n nodes (one-pass solution)
        # 1. Move 'fast' pointer n+1 steps ahead of 'slow' (starting from dummy)
        # 2. Move both pointers together until 'fast' reaches the end
        # 3. At this point, 'slow' is right before the node to remove
        # 4. Bypass that node
        
        slow = dummy
        fast = dummy
        
        # Advance fast pointer n+1 steps ahead
        # (n+1 so that slow ends up just BEFORE the node to remove)
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers until fast reaches the end (None)
        while fast:
            slow = slow.next
            fast = fast.next
        
        # slow is now the node just before the one we want to remove
        # Bypass the target node
        slow.next = slow.next.next
        
        # Return the real head (dummy.next), in case the original head was removed
        return dummy.next

#########
## EOF ##
#########