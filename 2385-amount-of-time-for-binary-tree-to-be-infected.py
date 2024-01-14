# 2385. Amount of Time for Binary Tree to Be Infected

# Medium

# You are given the root of a binary tree with unique values, and an
# integer start. At minute 0, an infection starts from the node with
# value start.

# Each minute, a node becomes infected if:

# The node is currently uninfected. The node is adjacent to an infected
# node. Return the number of minutes needed for the entire tree to be
# infected.

# Example 1:
# Input: root = [1,5,3,null,4,10,6,9,2], start = 3
# Output: 4
# Explanation: The following nodes are infected during:
# - Minute 0: Node 3
# - Minute 1: Nodes 1, 10 and 6
# - Minute 2: Node 5
# - Minute 3: Node 4
# - Minute 4: Nodes 9 and 2
# It takes 4 minutes for the whole tree to be infected so we return 4.

# Example 2:
# Input: root = [1], start = 1
# Output: 0
# Explanation: At minute 0, the only node in the tree is infected so we
# return 0.

# Constraints:
# The number of nodes in the tree is in the range [1, 10^5].
# 1 <= Node.val <= 10^5
# Each node has a unique value.
# A node with a value of start exists in the tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
from collections import defaultdict, deque


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        dq = deque()
        dq.append(root)

        while dq:
            l = len(dq)
            while l:
                node = dq.popleft()
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                    dq.append(node.left)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                    dq.append(node.right)
                l -= 1

        visited = set()

        def dfs(node, deep):
            visited.add(node)
            children = graph[node]
            res = deep
            for c in children:
                if c not in visited:
                    res = max(res, dfs(c, deep + 1))
            return res

        return dfs(start, 0)
