# 341. Flatten Nested List Iterator

# Medium

# You are given a nested list of integers nestedList. Each element is
# either an integer or a list whose elements may also be integers or
# other lists. Implement an iterator to flatten it.

# Implement the NestedIterator class:

# NestedIterator(List<NestedInteger> nestedList) Initializes the
# iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the
# nested list and false otherwise.


# Example 1:
# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]

# Explanation: By calling next repeatedly until hasNext returns false,
# the order of elements returned by next should be: [1,1,2,1,1].

# Example 2:
# Input: nestedList = [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false,
# the order of elements returned by next should be: [1,4,6].

# Constraints:
# 1 <= nestedList.length <= 500
# The values of the integers in the nested list is in the range [-106, 106].

from typing import List

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#     def isInteger(self) -> bool:
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         """
#         pass

#     def getInteger(self) -> int:
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         """
#         pass

#     def getList(self) -> List[NestedInteger]:
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         """
#         pass


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = list(reversed(nestedList))

    def next(self) -> int:
        self.unpack_list()
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        self.unpack_list()
        return len(self.stack) > 0

    def unpack_list(self):
        while self.stack and not self.stack[-1].isInteger():
            self.stack.extend(reversed(self.stack.pop().getList()))


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())