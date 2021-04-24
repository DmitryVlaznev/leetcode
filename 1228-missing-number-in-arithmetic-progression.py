# 1228. Missing Number In Arithmetic Progression

# Easy

# In some array arr, the values were in arithmetic progression: the
# values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length -
# 1.

# Then, a value from arr was removed that was not the first or last
# value in the array.

# Return the removed value.

# Example 1:
# Input: arr = [5,7,11,13]
# Output: 9
# Explanation: The previous array was [5,7,9,11,13].

# Example 2:
# Input: arr = [15,13,12]
# Output: 14
# Explanation: The previous array was [15,14,13,12].

# Constraints:
# 3 <= arr.length <= 1000
# 0 <= arr[i] <= 10^5

from typing import List
from utils import checkValue


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = int(arr[-1] - arr[0]) / len(arr)
        if diff == 0:
            return arr[0]
        l, r = 0, len(arr)
        while r - l > 1:
            mid = l + (r - l) // 2
            if (arr[mid] - arr[0]) / mid == diff:
                l = mid
            else:
                r = mid
        return int(arr[r] - diff)


t = Solution()

checkValue(9, t.missingNumber([5, 7, 11, 13]))
checkValue(14, t.missingNumber([15, 13, 12]))
checkValue(13, t.missingNumber([15, 14, 12]))
checkValue(14, t.missingNumber([15, 13]))
checkValue(0, t.missingNumber([0, 0, 0, 0, 0]))
checkValue(4, t.missingNumber([1, 2, 3, 5]))
checkValue(6, t.missingNumber([1, 2, 3, 4, 5, 7, 8]))
