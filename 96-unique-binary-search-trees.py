# 96. Unique Binary Search Trees

# Given n, how many structurally unique BST's (binary search trees) that
# store values 1 ... n?

# Example:

# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            m, last, acc = i // 2, i % 2 or 2, 0
            for k in range(i - 1, m - 1, -1):
                mul = dp[k] * dp[i - k - 1]
                acc += (mul * 2 if k != m else mul * last)
            dp[i] = acc
        return dp[n]

def log(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


t = Solution()

log(1, t.numTrees(1))
log(2, t.numTrees(2))
log(5, t.numTrees(3))
log(14, t.numTrees(4))
log(42, t.numTrees(5))
log(132, t.numTrees(6))
log(429, t.numTrees(7))