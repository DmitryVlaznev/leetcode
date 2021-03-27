# 916. Word Subsets

# Medium

# We are given two arrays A and B of words.  Each word is a string of
# lowercase letters.

# Now, say that word b is a subset of word a if every letter in b occurs
# in a, including multiplicity.  For example, "wrr" is a subset of
# "warrior", but is not a subset of "world".

# Now say a word a from A is universal if for every b in B, b is a
# subset of a.

# Return a list of all universal words in A.  You can return the words
# in any order.

# Example 1:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
# Output: ["facebook","google","leetcode"]

# Example 2:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
# Output: ["apple","google","leetcode"]

# Example 3:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
# Output: ["facebook","google"]

# Example 4:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
# Output: ["google","leetcode"]

# Example 5:
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
# Output: ["facebook","leetcode"]


# Note:
# 1 <= A.length, B.length <= 10000
# 1 <= A[i].length, B[i].length <= 10
# A[i] and B[i] consist only of lowercase letters.
# All words in A[i] are unique: there isn't i != j with A[i] == A[j].

from typing import List
from utils import checkList, listToArray


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def letters(word):
            res = [0] * 26
            for l in word:
                res[ord(l) - ord("a")] += 1
            return res

        max_letters = [0] * 26
        for word in B:
            for i, c in enumerate(letters(word)):
                max_letters[i] = max(max_letters[i], c)
        res = []
        for word in A:
            if all(a >= b for a, b in zip(letters(word), max_letters)):
                res.append(word)
        return res


t = Solution()

A = ["amazon", "apple", "facebook", "google", "leetcode"]
B = ["e", "o"]
checkList(["facebook", "google", "leetcode"], t.wordSubsets(A, B))

A = ["amazon", "apple", "facebook", "google", "leetcode"]
B = ["l", "e"]
checkList(["apple", "google", "leetcode"], t.wordSubsets(A, B))

A = ["amazon", "apple", "facebook", "google", "leetcode"]
B = ["e", "oo"]
checkList(["facebook", "google"], t.wordSubsets(A, B))

A = ["amazon", "apple", "facebook", "google", "leetcode"]
B = ["lo", "eo"]
checkList(["google", "leetcode"], t.wordSubsets(A, B))

A = ["amazon", "apple", "facebook", "google", "leetcode"]
B = ["ec", "oc", "ceo"]
checkList(["facebook", "leetcode"], t.wordSubsets(A, B))