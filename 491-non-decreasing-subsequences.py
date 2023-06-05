# 491. Non-decreasing Subsequences

# Medium
 
# Given an integer array nums, return all the different possible
# non-decreasing subsequences of the given array with at least two
# elements. You may return the answer in any order.

 

# Example 1:
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

# Example 2:
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]
 

# Constraints:

# 1 <= nums.length <= 15
# -100 <= nums[i] <= 100

from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def dfs(path, i):
            if i == len(nums):
                if len(path) > 1:
                    res.add(tuple(path))
                return
            if not path:
                dfs(path + nums[i:i+1], i+1)
            elif path and path[-1] <= nums[i]:
                dfs(path + nums[i:i+1], i+1)
            
            dfs(path, i+1)
        
        dfs([], 0)

        return [list(t) for t in res]

