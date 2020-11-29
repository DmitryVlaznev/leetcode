# 337. House Robber III

# Medium

# The thief has found himself a new place for his thievery again. There
# is only one entrance to this area, called the "root." Besides the
# root, each house has one and only one parent house. After a tour, the
# smart thief realized that "all houses in this place forms a binary
# tree". It will automatically contact the police if two directly-linked
# houses were broken into on the same night.

# Determine the maximum amount of money the thief can rob tonight
# without alerting the police.

# Example 1:
# Input: [3,2,3,null,3,null,1]
#      3
#     / \
#    2   3
#     \   \
#      3   1
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

# Example 2:
# Input: [3,4,5,1,3,null,1]
#      3
#     / \
#    4   5
#   / \   \
#  1   3   1
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

from utils import TreeNode, treeFromArray, checkValue


class Solution:
    def money_from_house(self, house: TreeNode) -> [int, int]:
        if not house:
            return 0, 0

        left = self.money_from_house(house.left)
        right = self.money_from_house(house.right)
        rob_this = house.val + left[1] + right[1]
        leave_this = max(left) + max(right)
        return rob_this, leave_this

    def rob(self, root: TreeNode) -> int:
        return max(self.money_from_house(root))
