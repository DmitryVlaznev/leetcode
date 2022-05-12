# 225. Implement Stack using Queues

# Easy

# Implement a last-in-first-out (LIFO) stack using only two queues. The
# implemented stack should support all the functions of a normal stack
# (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that
# only push to back, peek/pop from front, size and is empty operations
# are valid.

# Depending on your language, the queue may not be supported natively.
# You may simulate a queue using a list or deque (double-ended queue) as
# long as you use only a queue's standard operations.


# Example 1:
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False


# Constraints:

# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.


# Follow-up: Can you implement the stack using only one queue?


from collections import deque
from utils import checkValue


class MyStack:
    def __init__(self):
        self.dq = deque()

    def push(self, x: int) -> None:
        self.dq.append(x)
        c = len(self.dq) - 1
        while c:
            self.dq.append(self.dq.popleft())
            c -= 1

    def pop(self) -> int:
        return self.dq.popleft()

    def top(self) -> int:
        return self.dq[0]

    def empty(self) -> bool:
        return len(self.dq) == 0


# Definition for a double-linked list node.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None


class MyStack2:
    def __init__(self):
        self.head = self.tail = None

    def push(self, x: int) -> None:
        node = ListNode(x)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def pop(self) -> int:
        val = self.tail.val
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            t = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            t.prev = None
        return val

    def top(self) -> int:
        return self.tail.val

    def empty(self) -> bool:
        return self.head == None


myStack = MyStack()
myStack.push(1)
myStack.push(2)
checkValue(2, myStack.top())
checkValue(2, myStack.pop())
checkValue(False, myStack.empty())
