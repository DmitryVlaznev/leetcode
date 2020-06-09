# 406. Queue Reconstruction by Height

# Suppose you have a random list of people standing in a queue. Each
# person is described by a pair of integers (h, k), where h is the
# height of the person and k is the number of people in front of this
# person who have a height greater than or equal to h. Write an
# algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

# Example
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        import functools
        def comparator(a, b):
            if a[0] < b[0]: return -1
            if a[0] > b[0]: return 1
            if a[1] > b[1]: return -1
            if a[1] < b[1]: return 1
            return 0

        people.sort(key=functools.cmp_to_key(comparator))
        res = [None] * len(people)

        for h, k in people:
            c = -1
            for i, v in enumerate(res):
                if v is None: c += 1
                if c == k:
                    c = i
                    break
            res[c] = [h, k]
        return res

# print(people)
t = Solution()
print(t.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))