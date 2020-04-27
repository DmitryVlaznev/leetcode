# 146. LRU Cache

# Design and implement a data structure for Least Recently Used (LRU)
# cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the
# key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already
# present. When the cache reached its capacity, it should invalidate the
# least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

class CacheNode:
        def __init__(self, key, value):
            self.key = key
            self.value  = value
            self.prev = None
            self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.head = self.tail = None
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.hash: return -1
        item = self.hash[key]
        if self.head == item:
            # head, do nothing
            return item.value
        if item != self.tail:
            # middle
            item.prev.next = item.next
            item.next.prev = item.prev
        else:
            #tail
            self.tail = item.prev
            item.prev.next = None
        item.prev = None
        item.next = self.head
        self.head.prev = item
        self.head = item
        return item.value

    def put(self, key: int, value: int) -> None:
        if self.get(key) > -1:
            self.hash[key].value = value
            return

        item = CacheNode(key, value)
        if self.head == None:
            self.head = self.tail = item
        else:
            item.next = self.head
            self.head.prev = item
        self.hash[key] = item
        self.head = item
        self.size += 1

        if self.size > self.capacity:
            to_remove = self.tail
            to_remove.prev.next = None
            self.tail = to_remove.prev
            del self.hash[to_remove.key]
            del to_remove
            self.size -= 1

print("**************************************")
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print("1 = ", cache.get(1))
cache.put(3, 3)
print("-1 = ", cache.get(2))
cache.put(4, 4)
print("-1 = ", cache.get(1))
print("3 = ", cache.get(3))
print("4 = ", cache.get(4))

print("**************************************")
cache = LRUCache(1)
cache.put(1, 1)
cache.put(2, 2)
print("2 = ", cache.get(2))
print("-1 = ", cache.get(1))
cache.put(3, 3)
print("-1 = ", cache.get(2))
print("3 = ", cache.get(3))

print("**************************************")
cache = LRUCache(4)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
cache.put(4, 4)
cache.put(5, 5)
print("-1 = ", cache.get(1))
print("2 = ", cache.get(2))
print("4 = ", cache.get(4))
print("5 = ", cache.get(5))
cache.put(12, 12)
print("-1 = ", cache.get(3))
print("12 = ", cache.get(12))
print("2 = ", cache.get(2))
print("4 = ", cache.get(4))
print("5 = ", cache.get(5))
