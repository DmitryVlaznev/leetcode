# 173. Binary Search Tree Iterator

# Medium

# Implement the BSTIterator class that represents an iterator over the
# in-order traversal of a binary search tree (BST):

# BSTIterator(TreeNode root) Initializes an object of the BSTIterator
# class. The root of the BST is given as part of the constructor. The
# pointer should be initialized to a non-existent number smaller than
# any element in the BST. boolean hasNext() Returns true if there exists
# a number in the traversal to the right of the pointer, otherwise
# returns false. int next() Moves the pointer to the right, then returns
# the number at the pointer. Notice that by initializing the pointer to
# a non-existent smallest number, the first call to next() will return
# the smallest element in the BST.

# You may assume that next() calls will always be valid. That is, there
# will be at least a next number in the in-order traversal when next()
# is called.

# Example 1:
# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]

# Explanation
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
# bSTIterator.next();    // return 3
# bSTIterator.next();    // return 7
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 9
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 15
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 20
# bSTIterator.hasNext(); // return False


# Constraints:
# The number of nodes in the tree is in the range [1, 105].
# 0 <= Node.val <= 106
# At most 105 calls will be made to hasNext, and next.

# Follow up:
# Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?

from utils import TreeNode, checkValue, treeFromArray


class BSTIterator:
    root = None
    last = None
    path = None
    returned = 0

    def __init__(self, root: TreeNode):
        self.root = root
        self.path = []

    def go_left(self, node) -> int:
        p = node
        while p:
            self.path.append(p)
            p = p.left

    def next(self) -> int:
        self.returned += 1
        if not self.path:
            self.go_left(self.root)
            return self.path[-1].val

        if not self.path[-1].right:
            self.path.pop()
        else:
            self.go_left(self.path.pop().right)
        return self.path[-1].val

    def hasNext(self) -> bool:
        # print(self.path)
        if self.root and self.returned == 0:
            return True
        if len(self.path) > 1 or len(self.path) == 1 and self.path[0].right:
            return True
        return False


print("---------------------")
t = BSTIterator(treeFromArray([7, 3, 15, None, None, 9, 20], 0))
checkValue(3, t.next())
checkValue(7, t.next())
checkValue(True, t.hasNext())
checkValue(9, t.next())
checkValue(True, t.hasNext())
checkValue(15, t.next())
checkValue(True, t.hasNext())
checkValue(20, t.next())
checkValue(False, t.hasNext())

print("---------------------")
t = BSTIterator(treeFromArray([7], 0))
checkValue(True, t.hasNext())
checkValue(7, t.next())
checkValue(False, t.hasNext())

print("---------------------")
t = BSTIterator(treeFromArray([7, 5], 0))
checkValue(True, t.hasNext())
checkValue(5, t.next())
checkValue(True, t.hasNext())
checkValue(7, t.next())
checkValue(False, t.hasNext())

print("---------------------")
t = BSTIterator(treeFromArray([7, None, 5], 0))
checkValue(True, t.hasNext())
checkValue(7, t.next())
checkValue(True, t.hasNext())
checkValue(5, t.next())
checkValue(False, t.hasNext())

print("---------------------")
t = BSTIterator(
    treeFromArray([1, 2, 3, 6, 4, 8, 9, 7, None, None, 5, None, None, 10], 0)
)
checkValue(7, t.next())
checkValue(6, t.next())
checkValue(2, t.next())
checkValue(4, t.next())
checkValue(5, t.next())
checkValue(1, t.next())
checkValue(8, t.next())
checkValue(3, t.next())
checkValue(10, t.next())
checkValue(9, t.next())
checkValue(False, t.hasNext())

# bSTIterator.next();    // return 3
# bSTIterator.next();    // return 7
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 9
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 15
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 20
# bSTIterator.hasNext(); // return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()