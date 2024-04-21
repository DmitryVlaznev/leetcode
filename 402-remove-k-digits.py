# 402. Remove K Digits

# Given a non-negative integer num represented as a string, remove k
# digits from the number so that the new number is the smallest
# possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.

# Example 1:
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new
# number 1219 which is the smallest.

# Example 2:
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the
# output must not contain leading zeroes.

# Example 3:
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with
# nothing which is 0.


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and int(n) < stack[-1] and k:
                k -= 1
                stack.pop()
            stack.append(int(n))
        while k:
            stack.pop()
            k -= 1
        start = 0
        while start < len(stack) and stack[start] == 0:
            start += 1
        return "".join([str(n) for n in stack[start:]]) or "0"


def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()
log("0", t.removeKdigits("9", 1))
log("11", t.removeKdigits("112", 1))
log("1122", t.removeKdigits("11222", 1))
log("1219", t.removeKdigits("1432219", 3))
log("1111", t.removeKdigits("1112219", 3))
log("2219", t.removeKdigits("4442219", 3))
log("2219", t.removeKdigits("9242219", 3))
log("200", t.removeKdigits("10200", 1))
log("200", t.removeKdigits("105600025600", 5))
log("0", t.removeKdigits("200", 1))
log("0", t.removeKdigits("10", 2))
log("0", t.removeKdigits("12000003", 4))
log("3000000123", t.removeKdigits("12000003000000123", 2))
log("123", t.removeKdigits("12000003000000123", 3))
res = t.removeKdigits("112", 1)
log("11111191", t.removeKdigits("1119141191", 2))
log("111141191", t.removeKdigits("91119141191", 2))
log("111111191", t.removeKdigits("71118111191", 2))
log("145145691", t.removeKdigits("71458145691", 2))
log("14081405691", t.removeKdigits("7145081405691", 2))
