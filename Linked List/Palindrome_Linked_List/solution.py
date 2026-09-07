"""
PYTHON SOLUTION - Palindrome Linked List
08/11/2026
TIME COMPLEXITY: O(N)
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
    ## PALINDROME LINKED LIST  ##
    ##############################
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Empty list or single node is always a palindrome
        if not head or not head.next:
            return True
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: O(n) time, O(1) space using 3 steps
        # 1. Find the middle of the list using slow/fast pointers
        # 2. Reverse the second half of the list in-place
        # 3. Compare the first half against the reversed second half
        # (Optional 4th step: restore the list to its original structure)
        
        # STEP 1: Find the middle using slow/fast pointers
        # When fast reaches the end, slow is at the middle
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # STEP 2: Reverse the second half (starting from slow)
        second_half_head = self.reverse(slow)
        
        # Keep a reference to the reversed half's head for restoration later
        first_half_head = head
        second_half_copy = second_half_head
        
        # STEP 3: Compare first half against reversed second half
        result = True
        p1 = first_half_head
        p2 = second_half_head
        
        while p2:  # second half is same length or one shorter
            if p1.val != p2.val:
                result = False
                break
            p1 = p1.next
            p2 = p2.next
        
        # STEP 4 (optional but good practice): Restore original list structure
        self.reverse(second_half_copy)
        
        return result
    
    
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Helper function: reverses a linked list in-place, O(1) space."""
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        return prev

#########
## EOF ##
#########