"""
PYTHON SOLUTION - Merge Sorted Array
08/11/2026
TIME COMPLEXITY: O(M + N)
SPACE COMPLEXITY: O(1)
"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## MERGE          ##
    ####################
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ####################
        ## EDGE CASE      ##
        ####################
        # If nums2 is empty, nums1 already contains the correct merged result
        if n == 0:
            return
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Merge from the BACK, not the front!
        # nums1 has extra trailing space (the last n slots are placeholders),
        # so filling from the back avoids overwriting values we still need to read.
        #
        # Use three pointers:
        #   p1 -> last real element in nums1 (index m-1)
        #   p2 -> last element in nums2 (index n-1)
        #   p  -> last slot in nums1 overall (index m+n-1), where we WRITE
        #
        # At each step, place the LARGER of nums1[p1]/nums2[p2] at nums1[p],
        # then move that pointer (and p) backward.
        
        p1 = m - 1          # Pointer for last valid element in nums1
        p2 = n - 1          # Pointer for last element in nums2
        p = m + n - 1        # Pointer for where to write in nums1 (from the end)
        
        # Merge while both arrays still have unprocessed elements
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If nums2 still has remaining elements, copy them over
        # (If nums1 still has remaining elements, they're ALREADY in place
        #  since we're merging within nums1 itself - no action needed!)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

#########
## EOF ##
#########