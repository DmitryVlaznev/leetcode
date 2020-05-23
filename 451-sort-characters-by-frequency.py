# 451. Sort Characters By Frequency
# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:
# Input:
# "tree"
# Output:
# "eert"
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:
# Input:
# "cccaaa"
# Output:
# "cccaaa"
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:
# Input:
# "Aabb"
# Output:
# "bbAa"
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

class Solution:
    def frequencySort(self, s: str) -> str:
        # O(n)
        m, fr = 0, {}
        for l in s:
            fr[l] = 1 if l not in fr else fr[l] + 1
            m = max(m, fr[l])
        strings = [""] * (m + 1)
        for l, c in fr.items():
            strings[c] += "".join([l] * c)
        strings.reverse()
        return "".join(strings)

        # O(n log n)
        # pairs = Counter(s).most_common()
        # res = ""
        # for pair in pairs:
        #     res += "".join([pair[0]] * pair[1])
        # return res

t = Solution()
print(t.frequencySort("tree"))
print(t.frequencySort("cccaaa"))
print(t.frequencySort("Aabb"))
print(t.frequencySort("a"))
print(t.frequencySort(""))
