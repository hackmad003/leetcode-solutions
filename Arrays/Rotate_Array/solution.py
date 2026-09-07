"""
PYTHON SOLUTION - Rotate Array
12/28/2025 11:00 PM
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
"""

##############
## SOLUTION ##
##############
class Solution:
    
    ############
    ## ROTATE ##
    ############
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        ####################
        ## EDGE CASE      ##
        ####################
        # If array is empty or has one element, no rotation needed
        if n <= 1:
            return
        
        # Normalize k to handle cases where k > n
        k = k % n
        
        # If k is 0 after normalization, no rotation needed
        if k == 0:
            return
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Reverse three times
        # 1. Reverse entire array
        # 2. Reverse first k elements
        # 3. Reverse remaining n-k elements
        
        # Step 1: Reverse entire array
        self.reverse(nums, 0, n - 1)
        
        # Step 2: Reverse first k elements
        self.reverse(nums, 0, k - 1)
        
        # Step 3: Reverse remaining n-k elements
        self.reverse(nums, k, n - 1)
    
    ###########
    ## HELPER ##
    ###########
    def reverse(self, nums: list[int], start: int, end: int) -> None:
        """
        Helper function to reverse array from start to end (inclusive)
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

#########
## EOF ##
#########