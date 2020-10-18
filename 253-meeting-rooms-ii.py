# 253. Meeting Rooms II

# Given an array of meeting time intervals consisting of start and end
# times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of
# conference rooms required.

# Example 1:
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2

# Example 2:
# Input: [[7,10],[2,4]]
# Output: 1

# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.

#    Hide Hint #1
# Think about how we would approach this problem in a very simplistic
# way. We will allocate rooms to meetings that occur earlier in the day
# v/s the ones that occur later on, right?

#    Hide Hint #2
# If you've figured out that we have to sort the meetings by their start
# time, the next thing to think about is how do we do the allocation?
# There are two scenarios possible here for any meeting. Either there is
# no meeting room available and a new one has to be allocated, or a
# meeting room has freed up and this meeting can take place there.

#    Hide Hint #3
# An important thing to note is that we don't really care which room
# gets freed up while allocating a room for the current meeting. As long
# as a room is free, our job is done. We already know the rooms we have
# allocated till now and we also know when are they due to get free
# because of the end times of the meetings going on in those rooms. We
# can simply check the room which is due to get vacated the earliest
# amongst all the allocated rooms.

#    Hide Hint #4

# Following up on the previous hint, we can make use of a min-heap to
# store the end times of the meetings in various rooms.

# So, every time we want to check if any room is free or not, simply
# check the topmost element of the min heap as that would be the room
# that would get free the earliest out of all the other rooms currently
# occupied.

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        rooms = 0

        starts = sorted([i[0] for i in intervals])
        ends = sorted(i[1] for i in intervals)
        p = q = 0
        while p < len(intervals):
            if starts[p] >= ends[q]: rooms, q = rooms - 1, q + 1
            rooms, p = rooms + 1, p + 1
        return rooms