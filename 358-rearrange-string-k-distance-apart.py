# 358. Rearrange String k Distance Apart

# Hard

# Twitter, Google, Microsoft

# Given a string s and an integer k, rearrange s such that the same
# characters are at least distance k from each other. If it is not
# possible to rearrange the string, return an empty string "".

# Example 1:
# Input: s = "aabbcc", k = 3
# Output: "abcabc"
# Explanation: The same letters are at least a distance of 3 from each
# other.

# Example 2:
# Input: s = "aaabc", k = 3
# Output: ""
# Explanation: It is not possible to rearrange the string.

# Example 3:
# Input: s = "aaadbbcc", k = 2
# Output: "abacabcd"
# Explanation: The same letters are at least a distance of 2 from each
# other.


# Constraints:

# 1 <= s.length <= 3 * 10^5
# s consists of only lowercase English letters.
# 0 <= k <= s.length


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        from collections import deque, Counter
        import heapq

        h, dq, res = [], deque(), []
        for l, n in Counter(s).most_common():
            heapq.heappush(h, (-n, l))

        while len(res) < len(s):
            i = len(res)
            if len(dq) and i - dq[0][0] >= k:
                heapq.heappush(h, (dq[0][1], dq[0][2]))
                dq.popleft()

            if not len(h):
                return ""

            n, l = heapq.heappop(h)
            res.append(l)
            n += 1

            if n < 0:
                dq.append((i, n, l))

        return "".join(res)


s = Solution()
print(s.rearrangeString("aaabc", 3))
