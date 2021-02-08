# 284. Peeking Iterator

# Medium

# Given an Iterator class interface with methods: next() and hasNext(),
# design and implement a PeekingIterator that support the peek()
# operation -- it essentially peek() at the element that will be
# returned by the next call to next().

# Example:
# Assume that the iterator is initialized to the beginning of the list: [1,2,3].
# Call next() gets you 1, the first element in the list.
# Now you call peek() and it returns 2, the next element. Calling next()
# after that still return 2.
# You call next() the final time and it returns 3, the last element.
# Calling hasNext() after that should return false.
# Follow up: How would you extend your design to be generic and work
# with all types, not just integer?


from utils import checkValue


class Iterator:
    def __init__(self, nums):
        self.nums = nums
        self.index = -1

    def hasNext(self):
        return self.index < len(self.nums) - 1

    def next(self):
        self.index += 1
        return self.nums[self.index]


class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peeked = None

    def peek(self):
        if self.peeked is None:
            self.peeked = self.iterator.next()
        return self.peeked

    def next(self):
        if self.peeked is not None:
            t = self.peeked
            self.peeked = None
            return t
        return self.iterator.next()

    def hasNext(self):
        return self.peeked is not None or self.iterator.hasNext()


nums = [1, 2, 3]
iter = PeekingIterator(Iterator(nums))
checkValue(1, iter.peek())
checkValue(1, iter.peek())
checkValue(1, iter.peek())
checkValue(1, iter.next())
checkValue(2, iter.next())
checkValue(True, iter.hasNext())
checkValue(3, iter.peek())
checkValue(True, iter.hasNext())
checkValue(3, iter.next())
checkValue(False, iter.hasNext())


nums = []
iter = PeekingIterator(Iterator(nums))
checkValue(False, iter.hasNext())

nums = [1, 2, 3]
iter = PeekingIterator(Iterator(nums))
checkValue(1, iter.next())
checkValue(2, iter.next())
checkValue(3, iter.next())
checkValue(False, iter.hasNext())