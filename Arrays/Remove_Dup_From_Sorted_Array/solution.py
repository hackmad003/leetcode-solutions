"""
PYTHON SOLUTION - Remove Duplicates from Sorted Array
12/25/2025 10:00 PM
TIME COMPLEXITY: O(N)
SPACE COMPLEXITY: O(1)
"""

##############
## SOLUTION ##
##############
class Solution:
    
    #######################
    ## REMOVE DUPLICATES ##
    #######################
    def removeDuplicates(self, nums: list[int]) -> int:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # If Array has only one element, it's already unique
        if len(nums) <= 1:
            return len(nums)  # Return value of len(): The number of elements in the list
        
        # writeIndex points to where we should write the next unique element
        writeIndex = 1
        
        # Start from index 1 because the first element is always unique
        for i in range(1, len(nums)):
            # If current element is different from previous, it's unique
            if nums[i] != nums[i - 1]:
                nums[writeIndex] = nums[i]
                writeIndex += 1
        
        return writeIndex

#########
## EOF ##
#########