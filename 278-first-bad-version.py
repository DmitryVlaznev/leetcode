# 278. First Bad Version

# You are a product manager and currently leading a team to develop a
# new product. Unfortunately, the latest version of your product fails
# the quality check. Since each version is developed based on the
# previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out
# the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return
# whether version is bad. Implement a function to find the first bad
# version. You should minimize the number of calls to the API.

# Example:
# Given n = 5, and version = 4 is the first bad version.
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool

bad = 4
counter = 0

def isBadVersion(version):
    global counter
    global bad

    counter += 1
    return version >= bad

class Solution:
    def firstBadVersion(self, n):
        start = 1
        end = n
        while start <= end:
            mid = start + (end - start) // 2
            isBad = isBadVersion(mid)
            if isBad:
                if mid == 1 or isBadVersion(mid - 1) == False:
                    return mid
                else: end = mid - 1
            else:
                start = mid + 1

            # print("... start = ", start, "end = ", end, "mid = ", mid)
            # print("... isBad = ", isBad)
t = Solution()

bad = 4
counter = 0
print("4 = ", t.firstBadVersion(5))
print("calls = ", counter)
print("")

bad = 1
counter = 0
print("1 = ", t.firstBadVersion(5))
print("calls = ", counter)
print("")

bad = 5
counter = 0
print("5 = ", t.firstBadVersion(5))
print("calls = ", counter)
print("")

bad = 2
counter = 0
print("2 = ", t.firstBadVersion(4))
print("calls = ", counter)
print("")


bad = 2
counter = 0
print("2 = ", t.firstBadVersion(2))
print("calls = ", counter)
print("")

bad = 1
counter = 0
print("1 = ", t.firstBadVersion(2))
print("calls = ", counter)
print("")

bad = 1
counter = 0
print("1 = ", t.firstBadVersion(1))
print("calls = ", counter)
print("")

bad = 1024
counter = 0
print("1024 = ", t.firstBadVersion(100000))
print("calls = ", counter)
print("")

