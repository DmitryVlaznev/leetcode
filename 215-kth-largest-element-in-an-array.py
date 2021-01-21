# 215. Kth Largest Element in an Array

# Find the kth largest element in an unsorted array. Note that it is the
# kth largest element in the sorted order, not the kth distinct element.

# Example 1:
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5

# Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4

# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.


from typing import List


class Solution:
    def randomize(self, nums: List[int]):
        from random import randint

        for i in range(len(nums) - 1, 1, -1):
            random_index = randint(0, i - 2)
            nums[i], nums[random_index] = nums[random_index], nums[i]

    def partition(self, nums: List[int], start: int, end: int):
        lt = p = start
        k = nums[start]
        gt = end
        while p <= gt:
            if nums[p] > k:
                nums[p], nums[lt] = nums[lt], nums[p]
                p += 1
                lt += 1
            elif nums[p] < k:
                nums[p], nums[gt] = nums[gt], nums[p]
                gt -= 1
            else:
                p += 1
        return lt

    def findKthLargestQS(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]

        self.randomize(nums)
        start = 0
        end = len(nums) - 1
        ki = k - 1
        i = self.partition(nums, start, end)
        while i != ki:
            if i > ki:
                end = i - 1
            else:
                start = i + 1
            i = self.partition(nums, start, end)

        return nums[i]

    # max_heap
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        k_heap = nums[:k]
        heapq.heapify(k_heap)
        for n in nums[k:]:
            heapq.heappush(k_heap, n)
            heapq.heappop(k_heap)
        return heapq.heappop(k_heap)


test = Solution()

# arr = [1, 2]
# res = test.partition(arr, 0, len(arr) - 1)
# print(">>>>>>", res)
# print(arr)

# arr = [1, 2, 3]
# res = test.partition(arr, 0, len(arr) - 1)
# print(">>>>>>", res)
# print(arr)

# arr = [2, 1]
# res = test.partition(arr, 0, len(arr) - 1)
# print(">>>>>>", res)
# print(arr)

# arr = [3,2,3,1,2,4,5,5,6]
# res = test.partition(arr, 0, len(arr) - 1)
# print(">>>>>>", res)
# print(arr)


arr = [3, 2, 1, 5, 6, 4]
print("5 = ", test.findKthLargest(arr, 2))

arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print("4 = ", test.findKthLargest(arr, 4))

arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print("6 = ", test.findKthLargest(arr, 1))

arr = [1, 2]
print("1 = ", test.findKthLargest(arr, 2))

arr = [1, 2]
print("2 = ", test.findKthLargest(arr, 1))
