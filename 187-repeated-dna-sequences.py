# 187. Repeated DNA Sequences

# All DNA is composed of a series of nucleotides abbreviated as 'A',
# 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is
# sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings)
# that occur more than once in a DNA molecule.

# Example 1:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

# Example 2:
# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]

# Constraints:
# 0 <= s.length <= 105
# s[i] is 'A', 'C', 'G', or 'T'.

from typing import List
from utils import checkList

# Rabin-Karp
# hash[s[0..k]] = s[0]*p^(k-1) + s[i]*p^(k-i) + ... + s[k]*p^0
# hash(s[i + 1..i + m]) = (p⋅hash(s[i..i + m − 1]) − s[i]*p^m + s[i + m])

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if not s or len(s) < 11: return []
        letters = {"A": 0, "C": 1, "G": 2, "T": 3}
        m, hashes, res, p, cur_hash = 10, set(), set(), 17, 0
        for i, c in enumerate(s[0:m]): cur_hash += letters[c] * p ** (m - 1 - i)
        hashes.add(cur_hash)
        pw = p**(m - 1)

        for i in range(0, len(s) - m):
            cur_hash = (cur_hash - letters[s[i]] * pw) * p + letters[s[i + m]]
            if cur_hash in hashes: res.add(s[i + 1:i + m + 1])
            else: hashes.add(cur_hash)
        return list(res)

t = Solution()
checkList(["AAAAACCCCC","CCCCCAAAAA"], t.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
checkList(["AAAAAAAAAA"], t.findRepeatedDnaSequences("AAAAAAAAAAAAA"))