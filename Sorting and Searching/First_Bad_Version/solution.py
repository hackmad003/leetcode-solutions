"""
PYTHON SOLUTION - First Bad Version
08/11/2026
TIME COMPLEXITY: O(log N)
SPACE COMPLEXITY: O(1)
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

##############
## SOLUTION ##
##############
class Solution:
    
    ##########################
    ## FIRST BAD VERSION    ##
    ##########################
    def firstBadVersion(self, n: int) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Single version case: it must be the bad one (guaranteed by constraints)
        if n == 1:
            return 1
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Binary Search
        # The versions form a boolean sequence like: [False, False, ..., True, True]
        # (good, good, ..., bad, bad)
        # We want to find the FIRST "True" (first bad version) - a classic
        # "find first occurrence" binary search pattern.
        #
        # Narrow the search range each time based on isBadVersion(mid):
        #   - If mid is bad, the answer is mid OR something before it -> search left half
        #   - If mid is good, the answer must be after mid -> search right half
        
        left = 1
        right = n
        
        while left < right:
            mid = left + (right - left) // 2  # Avoids potential overflow
            
            if isBadVersion(mid):
                # mid is bad, so the first bad version is mid or earlier
                right = mid
            else:
                # mid is good, so the first bad version must be after mid
                left = mid + 1
        
        # When left == right, we've converged on the first bad version
        return left

#########
## EOF ##
#########