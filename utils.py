from typing import List

# Definition for a singly-linked list node.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a graph Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Utility functions


def graphFromArray(adj_list: List) -> Node:
    nodes = []
    for i in range(1, len(adj_list) + 1):
        nodes.append(Node(i))
    for i, adj in enumerate(adj_list):
        for n in adj:
            nodes[i].neighbors.append(nodes[n - 1])
    return nodes[0]


def listFromArray(values: List) -> ListNode:
    l = len(values)
    if not l:
        return None
    head = ListNode(values[0])
    cur = head
    for i in range(1, l):
        cur.next = ListNode(values[i])
        cur = cur.next
    return head


def listToArray(head: ListNode) -> List:
    arr = []
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    return arr


def treeToArray(root: TreeNode) -> List[int]:
    if not root:
        return []

    def find_max_depth(node: TreeNode, depth: int):
        """Find a max tree depth, counted from 1 (!!!)"""
        res = depth
        if node.left:
            res = max(res, find_max_depth(node.left, depth + 1))
        if node.right:
            res = max(res, find_max_depth(node.right, depth + 1))
        return res

    def fill_array(node: TreeNode, i: int, arr: List[int]):
        """A node index starts from 0 (for a root node)"""
        arr[i] = node.val
        if node.left:
            fill_array(node.left, 2 * i + 1, arr)
        if node.right:
            fill_array(node.right, 2 * i + 2, arr)
        return arr

    depth = find_max_depth(root, 1)
    max_nodes = (2 ** (depth + 1)) - 1

    res = fill_array(root, 0, [None] * max_nodes)
    while res[-1] == None:
        res.pop()
    return res


# The function below is incorrect
# Returns [10,5,15,2,7,None,25,None,None,6,None,20] for [10,5,15,2,7,None,25,None,None,6,None,None,None,20]

# def treeToArray(root: TreeNode) -> List[int]:
#     if not root: return []
#     def preorder(node: TreeNode, depth: int, traversal: List[List[int]]):
#         while len(traversal) <= depth: traversal.append([])
#         if node:
#             traversal[depth].append(node.val)
#             traversal = preorder(node.left, depth + 1, traversal)
#             traversal = preorder(node.right, depth + 1, traversal)
#         else:
#             traversal[depth].append(None)
#         return traversal
#     res = [item for sublist in preorder(root, 0, []) for item in sublist]
#     while res[-1] == None: res.pop()
#     return res


def treeFromArray(nodes: List[int], i: int = 0) -> TreeNode:
    l = len(nodes)
    node = TreeNode(nodes[i])
    ch_i = 2 * i + 1
    node.left = treeFromArray(nodes, ch_i) if ch_i < l and nodes[ch_i] != None else None
    ch_i += 1
    node.right = (
        treeFromArray(nodes, ch_i) if ch_i < l and nodes[ch_i] != None else None
    )
    return node


# Result checkers


def checkValue(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)


def checkList(correct, res):
    if len(correct) == len(res) and "".join(str(s) for s in correct) == "".join(
        str(s) for s in res
    ):
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)