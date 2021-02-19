# 784. Letter Case Permutation

# Medium

# Given a string S, we can transform every letter individually to be
# lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. You can return
# the output in any order.

# Example 1:
# Input: S = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]

# Example 2:
# Input: S = "3z4"
# Output: ["3z4","3Z4"]

# Example 3:
# Input: S = "12345"
# Output: ["12345"]

# Example 4:
# Input: S = "0"
# Output: ["0"]

# Constraints:
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.

from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = set()

        def mutate(i: int, current: List[str]):
            if i == len(S):
                res.add("".join(current))
                return
            mutate(i + 1, current + [(S[i]).upper()])
            mutate(i + 1, current + [(S[i]).lower()])

        mutate(0, [])
        return list(res)


t = Solution()

print(t.letterCasePermutation("a1b2"))
print(t.letterCasePermutation("3z4"))
print(t.letterCasePermutation("3Z4"))
print(t.letterCasePermutation("12345"))
print(t.letterCasePermutation("0"))