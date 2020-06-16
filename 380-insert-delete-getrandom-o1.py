# 380. Insert Delete GetRandom O(1)

# Design a data structure that supports all following operations in
# average O(1) time.

# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each
# element must have the same probability of being returned.

# Example:
# Init an empty set.
#   RandomizedSet randomSet = new RandomizedSet();
# Inserts 1 to the set. Returns true as 1 was inserted successfully.
#   randomSet.insert(1);
# Returns false as 2 does not exist in the set.
#   randomSet.remove(2);
# Inserts 2 to the set, returns true. Set now contains [1,2].
#   randomSet.insert(2);
# getRandom should return either 1 or 2 randomly.
#   randomSet.getRandom();
# Removes 1 from the set, returns true. Set now contains [2].
#   randomSet.remove(1);
# 2 was already in the set, so return false.
#   randomSet.insert(2);
# Since 2 is the only number in the set, getRandom always return 2.
#   randomSet.getRandom();


class RandomizedSet:
    def __init__(self):
        self.items = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:  return False
        self.items.append(val)
        self.indices[val] = len(self.items) - 1
        return True

    def remove(self, val: int) -> bool:
        if not val in self.indices: return False
        idx, last_idx = self.indices[val], len(self.items) - 1
        if idx == last_idx:
            self.items.pop()
            del self.indices[val]
            return True
        last_v = self.items[len(self.items) - 1]
        self.items[idx], self.items[last_idx] = (
            self.items[last_idx],
            self.items[idx],
        )
        self.items.pop()
        del self.indices[val]
        self.indices[last_v] = idx
        return True

    def getRandom(self) -> int:
        import random
        return self.items[int(random.random() * len(self.items))]


def log(correct, res):
    if correct == res: print("[v]", res)
    else: print(">>> INCORRECT >>>", correct, " | ", res)

print("---------------")
randomSet = RandomizedSet()
log(True, randomSet.insert(1))
log(False, randomSet.remove(2))
log(True, randomSet.insert(2))
print("1 or 2 = ", randomSet.getRandom())
log(True, randomSet.remove(1))
log(False, randomSet.insert(2))
log(2, randomSet.getRandom())
print("---------------")
print("")

randomSet = RandomizedSet()
log(False, randomSet.remove(0))
log(False, randomSet.remove(0))
log(True, randomSet.insert(0))
log(0, randomSet.getRandom())
log(True, randomSet.remove(0))
log(True, randomSet.insert(0))
print("---------------")
print("")

randomSet = RandomizedSet()
log(True, randomSet.insert(0))
log(True, randomSet.insert(1))
log(True, randomSet.remove(0))
log(True, randomSet.insert(2))
log(True, randomSet.remove(1))
log(2, randomSet.getRandom())
print("---------------")
print("")


