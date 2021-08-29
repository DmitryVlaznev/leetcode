# 537. Complex Number Multiplication

# Medium

# A complex number can be represented as a string on the form
# "real+imaginaryi" where:

# real is the real part and is an integer in the range [-100, 100].
# imaginary is the imaginary part and is an integer in the range [-100,
# 100].
# i^2 == -1.
# Given two complex numbers num1 and num2 as strings, return a string of
# the complex number that represents their multiplications.

# Example 1:
# Input: num1 = "1+1i", num2 = "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i^2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

# Example 2:
# Input: num1 = "1+-1i", num2 = "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i^2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

# Constraints:
# num1 and num2 are valid complex numbers.

from utils import checkValue


class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse(num: str):
            parts = num.split("+")
            return int(parts[0]), int(parts[1][0:-1] if len(parts[1]) > 1 else 0)

        r1, i1 = parse(num1)
        r2, i2 = parse(num2)
        real = r1 * r2 + -1 * i1 * i2
        imaginary = r1 * i2 + r2 * i1
        return str(real) + "+" + str(imaginary) + "i"