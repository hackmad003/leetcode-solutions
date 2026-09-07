"""
PYTHON SOLUTION - Maximum Subarray
08/11/2026
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ####################
    ## MAX SUBARRAY   ##
    ####################
    def maxSubArray(self, nums: List[int]) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Single element array: the answer is just that element
        if len(nums) == 1:
            return nums[0]
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Kadane's Algorithm (Dynamic Programming, single pass)
        # KEY INSIGHT: At each position, decide whether to:
        #   (a) EXTEND the previous subarray by including current element, OR
        #   (b) START FRESH with just the current element
        # Choose whichever gives a LARGER sum ending at this position.
        # Track the overall best sum seen across all positions.
        
        current_sum = nums[0]   # Best sum of a subarray ENDING at current position
        max_sum = nums[0]       # Best sum found so far, anywhere in the array
        
        for num in nums[1:]:
            # Either extend the previous subarray, or start a new one here
            current_sum = max(num, current_sum + num)
            
            # Update global best if this position's sum is better
            max_sum = max(max_sum, current_sum)
        
        return max_sum

#########
## EOF ##
#########











"""
PYTHON SOLUTION - Maximum Subarray (Divide and Conquer Approach)
08/11/2026
TIME COMPLEXITY: O(N log N)
SPACE COMPLEXITY: O(log N)
"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ##############################
    ## MAX SUBARRAY (D&C)       ##
    ##############################
    def maxSubArray(self, nums: List[int]) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        if len(nums) == 1:
            return nums[0]
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Divide and Conquer
        # Split array into left half and right half.
        # The max subarray is either:
        #   (a) Entirely in the LEFT half
        #   (b) Entirely in the RIGHT half
        #   (c) CROSSING the midpoint (spans both halves)
        # Take the max of all three possibilities.
        
        return self.divide_and_conquer(nums, 0, len(nums) - 1)
    
    
    def divide_and_conquer(self, nums: List[int], left: int, right: int) -> int:
        """Recursively finds the maximum subarray sum in nums[left..right]."""
        
        # Base case: single element
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        
        # Case (a): Best subarray entirely in the left half
        left_max = self.divide_and_conquer(nums, left, mid)
        
        # Case (b): Best subarray entirely in the right half
        right_max = self.divide_and_conquer(nums, mid + 1, right)
        
        # Case (c): Best subarray that CROSSES the midpoint
        cross_max = self.max_crossing_sum(nums, left, mid, right)
        
        # The answer is the best of all three cases
        return max(left_max, right_max, cross_max)
    
    
    def max_crossing_sum(self, nums: List[int], left: int, mid: int, right: int) -> int:
        """Finds the maximum sum of a subarray that crosses the midpoint,
        i.e., includes at least one element from both halves."""
        
        # Find the best sum extending LEFTWARD from mid (inclusive)
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, left - 1, -1):
            current_sum += nums[i]
            left_sum = max(left_sum, current_sum)
        
        # Find the best sum extending RIGHTWARD from mid+1 (inclusive)
        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid + 1, right + 1):
            current_sum += nums[i]
            right_sum = max(right_sum, current_sum)
        
        # Combine both halves - this is the best "crossing" subarray
        return left_sum + right_sum

#########
## EOF ##
#########