# 28. Implement strStr()

# Easy

# Return the index of the first occurrence of needle in haystack, or -1
# if needle is not part of haystack.

# Clarification:
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an
# empty string. This is consistent to C's strstr() and Java's indexOf().

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Example 3:
# Input: haystack = "", needle = ""
# Output: 0

# Constraints:
# 0 <= haystack.length, needle.length <= 5 * 10^4
# haystack and needle consist of only lower-case English characters.

# Rabin-Karp
# hash[s[0..k]] = s[0]*p^(k-1) + s[i]*p^(k-i) + ... + s[k]*p^0

from utils import checkValue


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k, l = len(needle), len(haystack)
        if not k:
            return 0
        if l < k:
            return -1
        if k == 1:
            for i, ll in enumerate(haystack):
                if ll == needle:
                    return i
            return -1
        if l == k:
            return 0 if haystack == needle else -1

        def is_collision(start):
            nonlocal haystack, needle
            for i in range(0, len(needle)):
                if needle[i] != haystack[start + i]:
                    return True
            return False

        letters = {chr(ord("a") + i): i for i in range(28)}
        h, hp, x, q = 0, 0, 17, 2 ** 31
        pw = (x ** (k - 1)) % q
        for i in range(0, k):
            hp += (letters[needle[i]] * (x ** (k - 1 - i))) % q
            h += (letters[haystack[i]] * (x ** (k - 1 - i))) % q

        for i in range(0, l - k + 1):
            if h == hp and not is_collision(i):
                return i
            if i < l - k:
                h = ((h - letters[haystack[i]] * pw) * x + letters[haystack[i + k]]) % q

        return -1


t = Solution()

checkValue(2, t.strStr("hello", "ll"))
checkValue(2, t.strStr("helloassdlls", "ll"))
checkValue(0, t.strStr("ll", "ll"))
checkValue(-1, t.strStr("hello", "llr"))
checkValue(0, t.strStr("hello", ""))
checkValue(0, t.strStr("", ""))
checkValue(-1, t.strStr("", "sdfsds"))
checkValue(2, t.strStr("abc", "c"))
checkValue(9, t.strStr("mississippi", "pi"))
checkValue(5, t.strStr("mississzippi", "ssz"))

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         k, l = len(needle), len(haystack)
#         if not k:
#             return 0
#         if l == k and haystack == needle:
#             return 0
#         if l < k:
#             return -1
#         if k == 1:
#             for i, ll in enumerate(haystack):
#                 if ll == needle:
#                     return i
#             return -1

#         def is_collision(start):
#             nonlocal haystack, needle
#             for i in range(0, len(needle)):
#                 if needle[i] != haystack[start + i]:
#                     return True
#             return False

#         def letter(l):
#             return ord(l) - ord("a")

#         h, hp, x = 0, 0, 17
#         pw = x ** (k - 1)
#         for i in range(0, k):
#             hp += letter(needle[i]) * (x ** (k - 1 - i))
#             h += letter(haystack[i]) * (x ** (k - 1 - i))

#         for i in range(0, l - k):
#             if h == hp and not is_collision(i):
#                 return i
#             h = (h - letter(haystack[i]) * pw) * x + letter(haystack[i + k])

#         return -1
