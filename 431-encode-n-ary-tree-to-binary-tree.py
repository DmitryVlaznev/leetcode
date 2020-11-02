# 431. Encode N-ary Tree to Binary Tree

# Design an algorithm to encode an N-ary tree into a binary tree and
# decode the binary tree to get the original N-ary tree. An N-ary tree
# is a rooted tree in which each node has no more than N children.
# Similarly, a binary tree is a rooted tree in which each node has no
# more than 2 children. There is no restriction on how your
# encode/decode algorithm should work. You just need to ensure that an
# N-ary tree can be encoded to a binary tree and this binary tree can be
# decoded to the original N-nary tree structure.

# Nary-Tree input serialization is represented in their level order
# traversal, each group of children is separated by the null value (See
# following example).

# For example, you may encode the following 3-ary tree to a binary tree
# in this way:

# Input: root = [1,null,3,2,4,null,5,6]

# Constraints:
# * The height of the n-ary tree is less than or equal to 1000
# * The total number of nodes is between [0, 10^4]
# * Do not use class member/global/static variables to store states.
#   Your encode and decode algorithms should be stateless.

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def encode(self, root):
        if not root:
            return None

        b_root = TreeNode(root.val)
        if root.children:
            b_root.left = self.encode(root.children[0])

        cur = b_root.left
        for c in root.children[1:]:
            cur.right = self.encode(c)
            cur = cur.right
        return b_root

    def decode(self, data):
        if not data:
            return None

        n_root = Node(data.val, [])

        cur = data.left
        while cur:
            n_root.children.append(self.decode(cur))
            cur = cur.right

        return n_root