# First Unique Number

# You have a queue of integers, you need to retrieve the first unique
# integer in the queue.

# Implement the FirstUnique class:

# FirstUnique(int[] nums) Initializes the object with the numbers in the
# queue. int showFirstUnique() returns the value of the first unique
# integer of the queue, and returns -1 if there is no such integer. void
# add(int value) insert value to the queue.


# Example 1:

# Input:
# ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
# [[[2,3,5]],[],[5],[],[2],[],[3],[]]
# Output:
# [null,2,null,2,null,3,null,-1]

# Explanation:
# FirstUnique firstUnique = new FirstUnique([2,3,5]);
# firstUnique.showFirstUnique(); // return 2
# firstUnique.add(5);            // the queue is now [2,3,5,5]
# firstUnique.showFirstUnique(); // return 2
# firstUnique.add(2);            // the queue is now [2,3,5,5,2]
# firstUnique.showFirstUnique(); // return 3
# firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
# firstUnique.showFirstUnique(); // return -1

# Example 2:

# Input:
# ["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
# [[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
# Output:
# [null,-1,null,null,null,null,null,17]

# Explanation:
# FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
# firstUnique.showFirstUnique(); // return -1
# firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
# firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
# firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
# firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
# firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
# firstUnique.showFirstUnique(); // return 17

# Example 3:

# Input:
# ["FirstUnique","showFirstUnique","add","showFirstUnique"]
# [[[809]],[],[809],[]]
# Output:
# [null,809,null,-1]

# Explanation:
# FirstUnique firstUnique = new FirstUnique([809]);
# firstUnique.showFirstUnique(); // return 809
# firstUnique.add(809);          // the queue is now [809,809]
# firstUnique.showFirstUnique(); // return -1

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^8
# 1 <= value <= 10^8
# At most 50000 calls will be made to showFirstUnique and add.

from typing import List

from collections import OrderedDict

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.queue = OrderedDict()
        self.processed = {}
        for v in nums: self.add(v)

    def showFirstUnique(self) -> int:
        return next(iter(self.queue)) if len(self.queue) else -1

    def add(self, value: int) -> None:
        if value in self.processed:
            if self.processed[value] == True:
                self.processed[value] = False
                del self.queue[value]
        else:
            self.processed[value] = True
            self.queue[value] = True

t = FirstUnique([2,3,5])
print("2 = ", t.showFirstUnique())
t.add(5)
print("2 = ", t.showFirstUnique())
t.add(2)
print("3 = ", t.showFirstUnique())
t.add(3)
print("-1 = ", t.showFirstUnique())


t = FirstUnique([233])
print("233 = ", t.showFirstUnique())
t.add(11)
print("233 = ", t.showFirstUnique())
