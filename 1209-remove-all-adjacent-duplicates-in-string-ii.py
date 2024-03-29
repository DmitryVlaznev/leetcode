# 1209. Remove All Adjacent Duplicates in String II

# Medium

# Given a string s, a k duplicate removal consists of choosing k
# adjacent and equal letters from s and removing them causing the left
# and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been
# made.

# It is guaranteed that the answer is unique.

# Example 1:
# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.

# Example 2:
# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation:
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"

# Example 3:
# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"

# Constraints:
# 1 <= s.length <= 10^5
# 2 <= k <= 10^4
# s only contains lower case English letters.

from utils import checkValue


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for l in s:
            if not stack:
                stack.append((l, 1))
                continue

            last, count = stack[-1]
            if last != l:
                stack.append((l, 1))
            else:
                if count + 1 == k:
                    while count:
                        stack.pop()
                        count -= 1
                else:
                    stack.append((l, count + 1))
        return "".join(map(lambda i: i[0], stack))


t = Solution()

checkValue("abcd", t.removeDuplicates("abcd", 2))
checkValue("a", t.removeDuplicates("a", 42))
checkValue("aa", t.removeDuplicates("deeedbbcccbdaa", 3))
checkValue("ps", t.removeDuplicates("pbbcggttciiippooaais", 2))