# 17. Letter Combinations of a Phone Number

# Medium

# Given a string containing digits from 2-9 inclusive, return all
# possible letter combinations that the number could represent. Return
# the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is
# given below. Note that 1 does not map to any letters.


# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

from typing import List
from utils import checkList


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []

        def backtrack(currentString, idx):
            if idx == len(digits):
                res.append("".join(currentString))
                return

            for l in letters[digits[idx]]:
                currentString.append(l)
                backtrack(currentString, idx + 1)
                currentString.pop()

        backtrack([], 0)
        return res


t = Solution()

checkList(
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], t.letterCombinations("23")
)
checkList([], t.letterCombinations(""))
checkList(["a", "b", "c"], t.letterCombinations("2"))
