# 170. Two Sum III - Data structure design

# Design a data structure that accepts integers of a stream, and checks
# if it has a pair of integers that sum up to a particular value.

# Implement a TwoSum class:

# TwoSum() Initializes the TwoSum object, with an empty array initially.
# void add(int number) Adds number to the data structure.
# boolean find(int value) Returns true if there exists any pair of
# numbers whose sum is equal to value, otherwise, it returns false.

# Example 1:
# Input
# ["TwoSum", "add", "add", "add", "find", "find"]
# [[], [1], [3], [5], [4], [7]]
# Output
# [null, null, null, null, true, false]

# Explanation
# TwoSum twoSum = new TwoSum();
# twoSum.add(1);   // [] --> [1]
# twoSum.add(3);   // [1] --> [1,3]
# twoSum.add(5);   // [1,3] --> [1,3,5]
# twoSum.find(4);  // 1 + 3 = 4, return True
# twoSum.find(7);  // No two integers sum up to 7, return False

# Constraints:
# -105 <= number <= 105
# -231 <= value <= 231 - 1
# At most 5 * 104 calls will be made to add and find.

class TwoSum:
    def __init__(self):
        self.seen = {}

    def add(self, number: int) -> None:
        if number in self.seen: self.seen[number] +=1
        else: self.seen[number] =1

    def find(self, value: int) -> bool:
        for n in self.seen.keys():
            if value - n in self.seen:
                if value - n != n: return True
                else:
                    if self.seen[n] > 1: return True
        return False

from utils import checkValue

t = TwoSum()
t.add(1)
t.add(3)
t.add(5)
checkValue(True, t.find(4))
checkValue(False, t.find(7))