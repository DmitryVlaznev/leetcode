# 703. Kth Largest Element in a Stream

# Design a class to find the kth largest element in a stream. Note that
# it is the kth largest element in the sorted order, not the kth
# distinct element.

# Your KthLargest class will have a constructor which accepts an integer
# k and an integer array nums, which contains initial elements from the
# stream. For each call to the method KthLargest.add, return the element
# representing the kth largest element in the stream.

# Example:

# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
# Note:
# You may assume that nums' length ≥ k-1 and k ≥ 1.

from typing import List


class KthLargest:
    heap = None
    size = -1
    target = None

    def __init__(self, k: int, nums: List[int]):
        self.target = k
        self.size = 0
        self.heap = [None] * (k + 2)

        for n in nums: self.add(n)

    def swim(self, index):
        parent = index // 2
        while index > 1 and self.heap[parent] > self.heap[index]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = index // 2

    def sink(self, index):
        while index * 2 <= self.size:
            ci = index * 2
            if ci + 1 <= self.size and self.heap[ci + 1] < self.heap[ci]: ci += 1
            if self.heap[index] <= self.heap[ci]: break

            self.heap[ci], self.heap[index] = self.heap[index], self.heap[ci]
            index = ci

    def add(self, val: int) -> int:
        if self.size >= self.target and val <= self.heap[1]:
            return self.heap[1]

        self.size += 1
        self.heap[self.size] = val
        self.swim(self.size)

        if self.size > self.target:
            self.heap[1] = self.heap[self.size]
            self.size -= 1
            self.sink(1)

        return self.heap[1]


print("--------------------------")
k = 3
arr = [4,5,8,2]
kthLargest = KthLargest(k, arr)
print("4 = ", kthLargest.add(3))
print("5 = ", kthLargest.add(5))
print("5 = ", kthLargest.add(10))
print("8 = ", kthLargest.add(9))
print("8 = ", kthLargest.add(4))

print("")
print("--------------------------")
k = 1
arr = []
kthLargest = KthLargest(k, arr)
print("-3 = ", kthLargest.add(-3))
print("-2 = ", kthLargest.add(-2))
print("-2 = ", kthLargest.add(-4))
print("0 = ", kthLargest.add(0))
print("4 = ", kthLargest.add(4))

print("")
print("--------------------------")
k = 7
arr = [-10,1,3,1,4,10,3,9,4,5,1]
kthLargest = KthLargest(k, arr)
print("3 = ", kthLargest.add(3))
print("3 = ", kthLargest.add(2))
print("3 = ", kthLargest.add(3))
print("3 = ", kthLargest.add(1))
print("3 = ", kthLargest.add(2))
print("3 = ", kthLargest.add(4))
print("4 = ", kthLargest.add(5))
print("4 = ", kthLargest.add(5))
print("4 = ", kthLargest.add(6))
print("5 = ", kthLargest.add(7))
print("5 = ", kthLargest.add(7))
print("5 = ", kthLargest.add(8))
print("5 = ", kthLargest.add(2))
print("5 = ", kthLargest.add(3))
print("5 = ", kthLargest.add(1))
print("5 = ", kthLargest.add(1))
print("5 = ", kthLargest.add(1))
print("6 = ", kthLargest.add(10))
print("7 = ", kthLargest.add(11))
print("7 = ", kthLargest.add(5))
print("7 = ", kthLargest.add(6))
print("7 = ", kthLargest.add(2))
print("7 = ", kthLargest.add(4))
print("7 = ", kthLargest.add(7))
print("7 = ", kthLargest.add(8))
print("7 = ", kthLargest.add(5))
print("7 = ", kthLargest.add(6))

