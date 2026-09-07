"""
PYTHON SOLUTION - Linked List Cycle
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
"""
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

##############
## SOLUTION ##
##############
class Solution:
    
    ######################
    ## HAS CYCLE        ##
    ######################
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Empty list or single node with no self-loop cannot have a cycle
        # (handled naturally by the main loop below, but stated for clarity)
        if not head or not head.next:
            return False
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Floyd's Cycle Detection (Tortoise and Hare)
        # Use two pointers moving at different speeds:
        #   slow moves 1 step at a time
        #   fast moves 2 steps at a time
        # If there's a cycle, fast will eventually "lap" slow and they meet
        # If there's no cycle, fast will reach the end (None) first
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # Move slow 1 step
            fast = fast.next.next     # Move fast 2 steps
            
            # If they ever meet, a cycle exists
            if slow == fast:
                return True
        
        # fast reached the end (None) without meeting slow -> no cycle
        return False

#########
## EOF ##
#########