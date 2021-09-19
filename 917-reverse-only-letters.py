# 917. Reverse Only Letters

# Easy

# Given a string s, reverse the string according to the following rules:
# All the characters that are not English letters remain in the same
# position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

# Example 1:
# Input: s = "ab-cd"
# Output: "dc-ba"

# Example 2:
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"

# Example 3:
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

# Constraints:
# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr = [l for l in s]
        p, q = 0, len(arr) - 1
        while p < q:
            if arr[p].isalpha() and arr[q].isalpha():
                arr[p], arr[q] = arr[q], arr[p]
                p, q = p + 1, q - 1
                continue
            if not arr[p].isalpha():
                p += 1
            if not arr[q].isalpha():
                q -= 1
        return "".join(arr)