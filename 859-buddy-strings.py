# 859. Buddy Strings

# Given two strings A and B of lowercase letters, return true if you can
# swap two letters in A so the result is equal to B, otherwise, return
# false.

# Swapping letters is defined as taking two indices i and j (0-indexed)
# such that i != j and swapping the characters at A[i] and A[j]. For
# example, swapping at indices 0 and 2 in "abcd" results in "cbad".

# Example 1:
# Input: A = "ab", B = "ba"
# Output: true
# Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.

# Example 2:
# Input: A = "ab", B = "ab"
# Output: false
# Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.

# Example 3:
# Input: A = "aa", B = "aa"
# Output: true
# Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.

# Example 4:
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true

# Example 5:
# Input: A = "", B = "aa"
# Output: false

# Constraints:
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist of lowercase letters.

from utils import checkValue

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False

        diff = []
        for i in range(0, len(A)):
            if A[i] != B[i]: diff.append(i)

        if len(diff) == 2:
            if A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
                return True
        elif len(diff) == 0:
            from collections import Counter
            counts = Counter(A)
            for key in counts.keys():
                if counts[key] > 1: return True

        return False

t = Solution()

checkValue(True, t.buddyStrings("ab", "ba"))
checkValue(False, t.buddyStrings("ab", "ab"))
checkValue(True, t.buddyStrings("aa", "aa"))
checkValue(True, t.buddyStrings("aaaaaaabc", "aaaaaaacb"))
checkValue(False, t.buddyStrings("", "aa"))