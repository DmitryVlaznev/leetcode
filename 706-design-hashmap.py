# 706. Design HashMap

# Easy

# Design a HashMap without using any built-in hash table libraries.

# To be specific, your design should include these functions:

# * put(key, value) : Insert a (key, value) pair into the HashMap. If
#   the value already exists in the HashMap, update the value.
# * get(key): Returns the value to which the specified key is mapped, or
#   -1 if this map contains no mapping for the key.
# * remove(key) : Remove the mapping for the value key if this map
#   contains the mapping for the key.

# Example:
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);
# hashMap.put(2, 2);
# hashMap.get(1);            // returns 1
# hashMap.get(3);            // returns -1 (not found)
# hashMap.put(2, 1);          // update the existing value
# hashMap.get(2);            // returns 1
# hashMap.remove(2);          // remove the mapping for 2
# hashMap.get(2);            // returns -1 (not found)

# Note:
# All keys and values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashMap library.


class MyHashMap:
    def __init__(self):
        self.keys = 10000
        self.table = [[] for _ in range(self.keys)]

    def put(self, key: int, value: int) -> None:
        pairs = self.table[key % self.keys]
        for pair in pairs:
            if key == pair[0]:
                pair[1] = value
                return
        pairs.append([key, value])

    def get(self, key: int) -> int:
        pairs = self.table[key % self.keys]
        for k, v in pairs:
            if key == k:
                return v
        return -1

    def remove(self, key: int) -> None:
        pairs = self.table[key % self.keys]
        for i, pair in enumerate(pairs):
            if key == pair[0]:
                del pairs[i]
                return
