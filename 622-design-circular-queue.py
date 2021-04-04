# 622. Design Circular Queue

# Medium

# Design your implementation of the circular queue. The circular queue
# is a linear data structure in which the operations are performed based
# on FIFO (First In First Out) principle and the last position is
# connected back to the first position to make a circle. It is also
# called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of
# the spaces in front of the queue. In a normal queue, once the queue
# becomes full, we cannot insert the next element even if there is a
# space in front of the queue. But using the circular queue, we can use
# the space to store new values.

# Implementation the MyCircularQueue class:

# * MyCircularQueue(k) Initializes the object with the size of the queue
#   to be k.
# * int Front() Gets the front item from the queue. If the queue is
#   empty, return -1.
# * int Rear() Gets the last item from the queue. If the queue is empty,
#   return -1.
# * boolean enQueue(int value) Inserts an element into the circular
#   queue. Return true if the operation is successful.
# * boolean deQueue() Deletes an element from the circular queue. Return
#   true if the operation is successful.
# * boolean isEmpty() Checks whether the circular queue is empty or not.
# * boolean isFull() Checks whether the circular queue is full or not.


# Example 1:
# Input
# ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue",
# "Rear", "isFull", "deQueue", "enQueue", "Rear"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]
# Output
# [null, true, true, true, false, 3, true, true, true, 4]

# Explanation
# MyCircularQueue myCircularQueue = new MyCircularQueue(3);
# myCircularQueue.enQueue(1); // return True
# myCircularQueue.enQueue(2); // return True
# myCircularQueue.enQueue(3); // return True
# myCircularQueue.enQueue(4); // return False
# myCircularQueue.Rear();     // return 3
# myCircularQueue.isFull();   // return True
# myCircularQueue.deQueue();  // return True
# myCircularQueue.enQueue(4); // return True
# myCircularQueue.Rear();     // return 4


# Constraints:
# 1 <= k <= 1000
# 0 <= value <= 1000
# At most 3000 calls will be made to enQueue, deQueue, Front, Rear,
# isEmpty, and isFull.

# Follow up: Could you solve the problem without using the built-in
# queue?


class MyCircularQueue:
    def __init__(self, k: int):
        self.front, self.rear, self.size, self.max_size = None, None, 0, k

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        node = {"val": value, "next": None}
        if self.size == 0:
            node["next"] = node
            self.front = node
            self.rear = node
        else:
            node["next"] = self.front
            self.rear["next"] = node
            self.rear = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        if self.size == 1:
            self.front, self.rear = None, None
        else:
            second = self.front["next"]
            self.rear["next"] = second
            self.front["next"] = None
            self.front = second
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.front["val"] if self.front else -1

    def Rear(self) -> int:
        return self.rear["val"] if self.rear else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


class MyCircularQueueDblLinked:
    def __init__(self, k: int):
        self.front, self.rear, self.size, self.max_size = None, None, 0, k

    def enQueue(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        node = {"val": value, "next": None, "prev": None}
        if self.size == 0:
            node["next"] = node
            node["prev"] = node
            self.front = node
            self.rear = node
        else:
            node["next"] = self.front
            node["prev"] = self.rear
            self.rear["next"] = node
            self.front["prev"] = node
            self.rear = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        if self.size == 1:
            self.front, self.rear = None, None
        else:
            second = self.front["next"]
            self.rear["next"] = second
            second["prev"] = self.rear
            self.front["next"] = None
            self.front["prev"] = None
            self.front = second
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.front["val"] if self.front else -1

    def Rear(self) -> int:
        return self.rear["val"] if self.rear else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


[
    "MyCircularQueue",
    "enQueue",
    "Rear",
    "Rear",
    "deQueue",
    "enQueue",
    "Rear",
    "deQueue",
    "Front",
    "deQueue",
    "deQueue",
    "deQueue",
]
[[6], [6], [], [], [], [5], [], [], [], [], [], []]

t = MyCircularQueue(6)
print(t.enQueue(6))
print(t.Rear())
print(t.Rear())
print(t.deQueue())
print(t.enQueue(5))
print(t.Rear())
print(t.deQueue())
print(t.isEmpty())
print(t.Front())
print(t.deQueue())
print(t.deQueue())
print(t.deQueue())
