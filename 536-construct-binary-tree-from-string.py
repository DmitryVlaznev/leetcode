# 536. Construct Binary Tree from String

# Medium

# You need to construct a binary tree from a string consisting of
# parenthesis and integers.

# The whole input represents a binary tree. It contains an integer
# followed by zero, one or two pairs of parenthesis. The integer
# represents the root's value and a pair of parenthesis contains a child
# binary tree with the same structure.

# You always start to construct the left child node of the parent first
# if it exists.

# Example 1:
# Input: s = "4(2(3)(1))(6(5))"
# Output: [4,2,6,3,1,5]

# Example 2:
# Input: s = "4(2(3)(1))(6(5)(7))"
# Output: [4,2,6,3,1,5,7]

# Example 3:
# Input: s = "-4(2(3)(1))(6(5)(7))"
# Output: [-4,2,6,3,1,5,7]

# Constraints:
# 0 <= s.length <= 3 * 104
# s consists of digits, '(', ')', and '-' only.

from utils import TreeNode, treeToArray, checkList


class Solution:
    def extractNodeData(self, s: str, start: int, end: int):
        if start > end:
            return None, None, None
        p = start
        while p <= end and (s[p] == "-" or s[p].isdigit()):
            p += 1
        value = int(s[start:p])

        if p > end or s[p] != "(":
            return value, None, None

        start = p = p + 1
        stack = ["("]
        while stack:
            if s[p] == "(":
                stack.append("(")
            elif s[p] == ")":
                stack.pop()
            p += 1
        left = (start, p - 1)

        if p > end or s[p] != "(":
            return value, left, None

        start = p = p + 1
        stack = ["("]
        while stack:
            if s[p] == "(":
                stack.append("(")
            elif s[p] == ")":
                stack.pop()
            p += 1
        right = (start, p - 1)

        return value, left, right

    def appendChildren(self, s, root, left, right):
        if left is not None:
            val, cl, cr = self.extractNodeData(s, left[0], left[1])
            if val is not None:
                root.left = TreeNode(val)
                self.appendChildren(s, root.left, cl, cr)
        if right is not None:
            val, cl, cr = self.extractNodeData(s, right[0], right[1])
            if val is not None:
                root.right = TreeNode(val)
                self.appendChildren(s, root.right, cl, cr)

    def str2tree(self, s: str) -> TreeNode:
        root_val, left, right = self.extractNodeData(s, 0, len(s) - 1)

        if root_val is None:
            return None
        root = TreeNode(root_val)

        self.appendChildren(s, root, left, right)

        return root


t = Solution()
checkList([4, 2, 6, 3, 1, 5], treeToArray(t.str2tree("4(2(3)(1))(6(5))")))
checkList([4, 2, 6, 3, 1, 5, 7], treeToArray(t.str2tree("4(2(3)(1))(6(5)(7))")))
checkList([-423, 2, None, 3, 1], treeToArray(t.str2tree("-423(2(3)(1))")))
checkList([4], treeToArray(t.str2tree("4")))
checkList([], treeToArray(t.str2tree("")))
