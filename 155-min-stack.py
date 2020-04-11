# Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.


# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.

class MinStack:
    stack = None
    min_stack = None

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)
        msl = len(self.min_stack)
        if not msl or self.min_stack[msl - 1] >= x:
            self.min_stack.append(x)


    def pop(self) -> None:
        if not len(self.stack):
            return None
        v = self.stack.pop()
        if self.min_stack[len(self.min_stack) - 1] == v:
            self.min_stack.pop()
        return v

    def top(self) -> int:
        l = len(self.stack)
        if not l:
            return None
        return self.stack[l - 1]

    def getMin(self) -> int:
        l = len(self.min_stack)
        if not l:
            return None
        return self.min_stack[l - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

print("------------------------")
t = MinStack()
print("None", t.pop())
print("None", t.top())
print("None", t.getMin())
t.push(-2)
t.push(0)
t.push(-3)
print("-3", t.getMin())
print("-3", t.pop())
print("0", t.top())
print("-2", t.getMin())
print("0", t.pop())
print("-2", t.top())
print("-2", t.getMin())
print("-2", t.pop())
print("None", t.top())
print("None", t.getMin())
print("None", t.pop())
print("")

print("------------------------")
t = MinStack()
t.push(5)
t.push(6)
t.push(7)
print("5", t.getMin())
t.push(0)
t.push(0)
t.push(3)
print("0", t.getMin())
t.push(0)
t.push(8)
print("0", t.getMin())
print("8", t.pop())
print("0", t.getMin())
print("0", t.pop())
print("3", t.pop())
print("0", t.getMin())
print("0", t.pop())
print("0", t.pop())
print("5", t.getMin())
print("")