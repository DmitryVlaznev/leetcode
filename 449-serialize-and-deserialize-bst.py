# 449. Serialize and Deserialize BST

# Serialization is converting a data structure or object into a sequence
# of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later
# in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary search tree.
# There is no restriction on how your serialization/deserialization
# algorithm should work. You need to ensure that a binary search tree
# can be serialized to a string, and this string can be deserialized to
# the original tree structure.

# The encoded string should be as compact as possible.


# Example 1:
# Input: root = [2,1,3]
# Output: [2,1,3]

# Example 2:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# 0 <= Node.val <= 104
# The input tree is guaranteed to be a binary search tree.

from utils import TreeNode, treeFromArray, treeToArray, checkValue, checkList

class Codec:

    def subtree(self, preorder, start, end):
        if start == end: return TreeNode(preorder[start])

        v = preorder[start]
        left_i = start + 1 if preorder[start + 1] < v else None

        import bisect
        right_i = (bisect.bisect(preorder, v, start + 1, end) if preorder[end] > v else None)
        node = TreeNode(v)
        if left_i is not None:
            branch_end = right_i - 1 if right_i is not None else end
            node.left = self.subtree(preorder, left_i, branch_end)
        if right_i is not None:
            node.right = self.subtree(preorder, right_i, end)
        return node

    def serialize(self, root: TreeNode) -> str:
        if not root: return ""

        def preorder(root):
            if not root: return []
            return [root.val] + preorder(root.left) + preorder(root.right)

        return "|".join(str(n) for n in preorder(root))

    def deserialize(self, data: str) -> TreeNode:
        if not data: return None

        arr = [int(s) for s in data.split("|")]
        return self.subtree(arr, 0, len(arr) - 1)

t = Codec()

checkValue("4|2|1|3|7|5", t.serialize(treeFromArray([4,2,7,1,3,5], 0)))
checkList([4,2,7,1,3,5], treeToArray(t.deserialize("4|2|1|3|7|5")))

checkValue("4|2|1|3|7|9", t.serialize(treeFromArray([4,2,7,1,3,None,9], 0)))
checkList([4,2,7,1,3,None,9], treeToArray(t.deserialize("4|2|1|3|7|9")))

checkValue("10|5|2|7|6|15|25|20", t.serialize(treeFromArray([10,5,15,2,7,None,25,None,None,6,None,None,None,20], 0)))
checkList([10,5,15,2,7,None,25,None,None,6,None,None,None,20], treeToArray(t.deserialize("10|5|2|7|6|15|25|20")))

# Postorder

# class Codec:
#     def serialize(self, root):
#         """
#         Encodes a tree to a single string.
#         """
#         def postorder(root):
#             return postorder(root.left) + postorder(root.right) + [root.val] if root else []
#         return ' '.join(map(str, postorder(root)))

#     def deserialize(self, data):
#         """
#         Decodes your encoded data to tree.
#         """
#         def helper(lower = float('-inf'), upper = float('inf')):
#             if not data or data[-1] < lower or data[-1] > upper:
#                 return None

#             val = data.pop()
#             root = TreeNode(val)
#             root.right = helper(val, upper)
#             root.left = helper(lower, val)
#             return root

#         data = [int(x) for x in data.split(' ') if x]
#         return helper()