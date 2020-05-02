# 771. Jewels and Stones

# You're given strings J representing the types of stones that are
# jewels, and S representing the stones you have.  Each character in S
# is a type of stone you have.  You want to know how many of the stones
# you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and
# S are letters. Letters are case sensitive, so "a" is considered a
# different type of stone from "A".

# Example 1:
# Input: J = "aA", S = "aAAbbbb"
# Output: 3

# Example 2:
# Input: J = "z", S = "ZZ"
# Output: 0

# Note:
# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = 0
        for c in J: jewels |= 1 << (ord(c) - 65)
        counter = 0
        for c in S:
            if jewels & 1 << (ord(c) - 65): counter += 1
        return counter

t = Solution()
print("3 = ", t.numJewelsInStones("aA", "aAAbbbb"))
print("0 = ", t.numJewelsInStones("z", "ZZ"))
print("0 = ", t.numJewelsInStones("", "ZZ"))
print("0 = ", t.numJewelsInStones("qwe", ""))
print("0 = ", t.numJewelsInStones("", ""))