# 273. Integer to English Words

# Hard

# Convert a non-negative integer num to its English words
# representation.

# Example 1:
# Input: num = 123
# Output: "One Hundred Twenty Three"

# Example 2:
# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"

# Example 3:
# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

# Example 4:
# Input: num = 2147483641
# Output: "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty One"


# Constraints:
# 0 <= num <= 2^31 - 1


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def parseTriplet(n):
            w_ones = [
                "One",
                "Two",
                "Three",
                "Four",
                "Five",
                "Six",
                "Seven",
                "Eight",
                "Nine",
            ]
            w_teens = [
                "Ten",
                "Eleven",
                "Twelve",
                "Thirteen",
                "Fourteen",
                "Fifteen",
                "Sixteen",
                "Seventeen",
                "Eighteen",
                "Nineteen",
            ]
            w_ties = [
                "Twenty",
                "Thirty",
                "Forty",
                "Fifty",
                "Sixty",
                "Seventy",
                "Eighty",
                "Ninety",
            ]
            d0 = n % 10
            d1 = (n % 100 - d0) // 10
            d2 = (n - d1 - d0) // 100

            res = []
            if d1 == 1:
                res.append(w_teens[d0])
            else:
                if d0 > 0:
                    res.append(w_ones[d0 - 1])
                if d1 > 1:
                    res.append(w_ties[d1 - 2])
            if d2 > 0:
                res.append(w_ones[d2 - 1] + " Hundred")
            res.reverse()
            return res

        ones = num % 1000
        thousands = (num % 1000000 - ones) // 1000
        millions = (num % 1000000000 - thousands - ones) // 1000000
        billions = (num - millions - thousands - ones) // 1000000000

        res = []

        if billions:
            res = res + parseTriplet(billions) + ["Billion"]
        if millions:
            res = res + parseTriplet(millions) + ["Million"]
        if thousands:
            res = res + parseTriplet(thousands) + ["Thousand"]
        if ones:
            res = res + parseTriplet(ones)

        return " ".join(res)


s = Solution()

print("12 = ", s.numberToWords(12))
print("20 = ", s.numberToWords(20))
print("123 = ", s.numberToWords(123))
print("12345 = ", s.numberToWords(12345))
print("1234567 = ", s.numberToWords(1234567))
print("120000 = ", s.numberToWords(120000))
print("2147483641 = ", s.numberToWords(2147483641))