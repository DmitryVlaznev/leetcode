# 784. Letter Case Permutation

# Given a string S, we can transform every letter individually to be
# lowercase or uppercase to create another string.  Return a list of all
# possible strings we could create.

# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

# Input: S = "3z4"
# Output: ["3z4", "3Z4"]

# Input: S = "12345"
# Output: ["12345"]
# Note:

# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.

from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not len(S):
            return []

        res = set()
        self.permutate(S.lower(), "", res)
        return list(res)

    def permutate(self, s: str, prefix: str, res: set):
        if not len(s):
            res.add(prefix)
            return

        letter = s[0:1]
        tmpstr = s[1:]
        self.permutate(tmpstr, prefix + letter, res)

        upper = letter.upper()
        if upper != letter:
            self.permutate(tmpstr, prefix + upper, res)

test = Solution()

print(["a1b2", "a1B2", "A1b2", "A1B2"])
print(test.letterCasePermutation("a1b2"))

print(["3z4", "3Z4"])
print(test.letterCasePermutation("3z4"))

print(["12345"])
print(test.letterCasePermutation("12345"))

print([])
print(test.letterCasePermutation(""))