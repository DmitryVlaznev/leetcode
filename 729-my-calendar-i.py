# 729. My Calendar I

# Medium

# Implement a MyCalendar class to store your events. A new event can be
# added if adding the event will not cause a double booking.

# Your class will have the method, book(int start, int end). Formally,
# this represents a booking on the half open interval [start, end), the
# range of real numbers x such that start <= x < end.

# A double booking happens when two events have some non-empty
# intersection (ie., there is some time that is common to both events.)

# For each call to the method MyCalendar.book, return true if the event
# can be added to the calendar successfully without causing a double
# booking. Otherwise, return false and do not add the event to the
# calendar.

# Your class will be called like this: MyCalendar cal = new
# MyCalendar(); MyCalendar.book(start, end)

# Example 1:
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(15, 25); // returns false
# MyCalendar.book(20, 30); // returns true
# Explanation:
# The first event can be booked.  The second can't because time 15 is
# already booked by another event.
# The third event can be booked, as the first event takes every time
# less than 20, but not including 20.

# Note:
# * The number of calls to MyCalendar.book per test case will be at most
#   1000.
# * In calls to MyCalendar.book(start, end), start and end are integers
#   in the range [0, 10^9].


from utils import checkValue


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False


class MyCalendar:
    def __init__(self):
        self.booked = None

    def book(self, start: int, end: int) -> bool:
        if self.booked is None:
            self.booked = Node(start, end)
            return True
        return self.booked.insert(Node(start, end))


s = MyCalendar()
checkValue(True, s.book(10, 20))
checkValue(False, s.book(15, 25))
checkValue(True, s.book(20, 30))

s = MyCalendar()
checkValue(True, s.book(47, 50))
checkValue(True, s.book(33, 41))
checkValue(False, s.book(39, 45))
checkValue(False, s.book(33, 42))
checkValue(True, s.book(25, 32))
checkValue(False, s.book(26, 35))
checkValue(True, s.book(19, 25))
checkValue(True, s.book(3, 8))
checkValue(True, s.book(8, 13))
checkValue(False, s.book(18, 27))

s = MyCalendar()
checkValue(True, s.book(20, 29))
checkValue(False, s.book(13, 22))
checkValue(True, s.book(44, 50))
checkValue(True, s.book(1, 7))
checkValue(False, s.book(2, 10))
checkValue(True, s.book(14, 20))
checkValue(False, s.book(19, 25))
checkValue(True, s.book(36, 42))
checkValue(False, s.book(45, 50))
checkValue(False, s.book(47, 50))
checkValue(False, s.book(39, 45))
checkValue(False, s.book(44, 50))
checkValue(False, s.book(16, 25))
checkValue(False, s.book(45, 50))
checkValue(False, s.book(45, 50))
checkValue(False, s.book(12, 20))
checkValue(False, s.book(21, 29))
checkValue(False, s.book(11, 20))
checkValue(False, s.book(12, 17))
checkValue(False, s.book(34, 40))
checkValue(False, s.book(10, 18))
checkValue(False, s.book(38, 44))
checkValue(False, s.book(23, 32))
checkValue(False, s.book(38, 44))
checkValue(False, s.book(15, 20))
checkValue(False, s.book(27, 33))
checkValue(False, s.book(34, 42))
checkValue(False, s.book(44, 50))
checkValue(False, s.book(35, 40))
checkValue(False, s.book(24, 31))