# 423. Reconstruct Original Digits from English

# Medium

# Given a non-empty string containing an out-of-order English
# representation of digits 0-9, output the digits in ascending order.

# Note:
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original
# digits. That means invalid inputs such as "abc" or "zerone" are not
# permitted.
# Input length is less than 50,000.

# Example 1:
# Input: "owoztneoer"
# Output: "012"

# Example 2:
# Input: "fviefuro"

# Output: "45"


from collections import Counter
from utils import checkValue


class Solution:
    def originalDigits(self, s: str) -> str:
        words = [
            "zero",
            "two",
            "four",
            "six",
            "eight",
            "one",
            "three",
            "five",
            "seven",
            "nine",
        ]
        digits = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        c = Counter(s)
        res = []
        for i, word in enumerate(words):
            count = float("inf")
            for l in word:
                if l in c and c[l] > 0:
                    count = min(count, c[l])
                else:
                    count = float("inf")
                    break
            if count == float("inf"):
                continue
            res += [digits[i]] * count
            for l in word:
                c[l] -= count
        res.sort()
        return "".join(str(n) for n in res)


t = Solution()

checkValue("012", t.originalDigits("owoztneoer"))
checkValue("45", t.originalDigits("fviefuro"))
checkValue("0123456789", t.originalDigits("zerotwofoursixeightonethreefivesevennine"))
checkValue("", t.originalDigits(""))
checkValue("9", t.originalDigits("nine"))
checkValue("00", t.originalDigits("zerozero"))
checkValue("00117777", t.originalDigits("zoneesesevenvenrozseveneonesevenro"))
