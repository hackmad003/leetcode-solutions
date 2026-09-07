"""
PYTHON SOLUTION - Intersection of Two Arrays II
12/28/2025 11:40 PM
TIME COMPLEXITY: O(M + N)
SPACE COMPLEXITY: O(MIN(M, N))

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

"""
from collections import Counter
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ###############
    ## INTERSECT ##
    ###############
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # If either array is empty, intersection is empty
        if not nums1 or not nums2:
            return []
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Use Counter to count frequencies
        # Count elements in smaller array for space efficiency
        
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # Count frequency of elements in nums1
        count = Counter(nums1)
        
        # Find intersections in nums2
        result = []
        
        for num in nums2:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1 # Each time we use a number, we burn one copy.
        
        return result

#########
## EOF ##
#########


"""
PYTHON SOLUTION - Intersection of Two Arrays II
12/28/2025 11:40 PM
TIME COMPLEXITY: O(M + N)
SPACE COMPLEXITY: O(MIN(M, N))
"""

from collections import Counter
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        count = {}
        for num in nums1:
            count[num] = count.get(num, 0) + 1
        
        result = []
        for num in nums2:
            if count.get(num, 0) > 0:
                result.append(num)
                count[num] -= 1
        
        return result

#########
## EOF ##
#########




"""
PYTHON SOLUTION - Intersection of Two Arrays II
12/28/2025 11:40 PM
TIME COMPLEXITY: O(M log M + N log N)
SPACE COMPLEXITY: O(1) (excluding output)
"""

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        result = []
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        
        return result

#########
## EOF ##
#########







"""
PYTHON SOLUTION - Intersection of Two Arrays II
12/28/2025 11:40 PM
TIME COMPLEXITY: O(M + N)
SPACE COMPLEXITY: O(min(M, N))
"""

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        count = {}
        for num in nums1:
            count[num] = count.get(num, 0) + 1
        
        result = []
        result_append = result.append
        count_get = count.get
        
        for num in nums2:
            c = count_get(num, 0)
            if c > 0:
                result_append(num)
                count[num] = c - 1
        
        return result

#########
## EOF ##
#########



"""
PYTHON SOLUTION - Intersection of Two Arrays II
TIME COMPLEXITY: O(M + N)
SPACE COMPLEXITY: O(min(M, N))
"""

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        count = {}
        for num in nums1:
            count[num] = count.get(num, 0) + 1
        
        result = []
        for num in nums2:
            if count.get(num, 0) > 0:
                result.append(num)
                count[num] -= 1
        
        return result

#########
## EOF ##
#########