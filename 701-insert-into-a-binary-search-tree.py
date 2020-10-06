# Insert into a Binary Search Tree

# You are given the root node of a binary search tree (BST) and a value
# to insert into the tree. Return the root node of the BST after the
# insertion. It is guaranteed that the new value does not exist in the
# original BST.

# Notice that there may exist multiple valid ways for the insertion, as
# long as the tree remains a BST after insertion. You can return any of
# them.


# Example 1:
# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:

# Example 2:
# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]
# Example 3:

# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]


# Constraints:
# The number of nodes in the tree will be in the range [0, 104].
# -108 <= Node.val <= 108
# All the values Node.val are unique.
# -108 <= val <= 108
# It's guaranteed that val does not exist in the original BST.

from utils import TreeNode, checkList, treeFromArray, treeToArray

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        p = root
        if not p: return TreeNode(val)
        while(True):
            if p.val < val:
                if not p.right:
                    p.right = TreeNode(val)
                    break
                else: p = p.right
            else:
                if not p.left:
                    p.left = TreeNode(val)
                    break
                else: p = p.left
        return root


# checkList([4,2,7,1,3], treeToArray(treeFromArray([4,2,7,1,3], 0)))
# checkList([40,20,60,10,30,50,70], treeToArray(treeFromArray([40,20,60,10,30,50,70], 0)))
# checkList([40,20,60,10,30,50,70,None,None,25], treeToArray(treeFromArray([40,20,60,10,30,50,70,None,None,25], 0)))

t = Solution()
checkList([4,2,7,1,3,5], treeToArray(t.insertIntoBST(treeFromArray([4,2,7,1,3], 0), 5)))
checkList([40,20,60,10,30,50,70,None,None,25], treeToArray(t.insertIntoBST(treeFromArray([40,20,60,10,30,50,70], 0), 25)))
checkList([42], treeToArray(t.insertIntoBST(None, 42)))
checkList([4,2,7,1,3,5], treeToArray(t.insertIntoBST(treeFromArray([4,2,7,1,3,None,None,None,None,None,None], 0), 5)))

