"""
PYTHON SOLUTION - Merge Two Sorted Lists
08/11/2026
TIME COMPLEXITY: O(N + M)
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
    
    ##########################
    ## MERGE TWO LISTS      ##
    ##########################
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # If one list is empty, the merged result is simply the other list
        if not list1:
            return list2
        if not list2:
            return list1
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Splice nodes together using a dummy head
        # Walk both lists simultaneously, always attaching the smaller
        # current node to the merged list, then advancing that list's pointer
        
        # Dummy node simplifies edge cases (no need to special-case the head)
        dummy = ListNode(0)
        tail = dummy
        
        # Walk both lists while both still have nodes remaining
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            # Advance the tail of the merged list
            tail = tail.next
        
        # Attach whichever list still has remaining nodes
        # (at most one of list1/list2 is non-empty at this point)
        tail.next = list1 if list1 else list2
        
        # Real merged list starts after the dummy node
        return dummy.next

#########
## EOF ##
#########