from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Utility functions

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
    if not root: return []
    def preorder(node: TreeNode, depth: int, traversal: List[List[int]]):
        while len(traversal) <= depth: traversal.append([])
        if node:
            traversal[depth].append(node.val)
            traversal = preorder(node.left, depth + 1, traversal)
            traversal = preorder(node.right, depth + 1, traversal)
        else:
            traversal[depth].append(None)
        return traversal
    res = [item for sublist in preorder(root, 0, []) for item in sublist]
    while res[-1] == None: res.pop()
    return res

def treeFromArray(nodes: List[int], i: int) -> TreeNode:
    l = len(nodes)
    node = TreeNode(nodes[i])
    ch_i = 2 * i + 1
    node.left = treeFromArray(nodes, ch_i) if ch_i < l and nodes[ch_i] != None else None
    ch_i += 1
    node.right = treeFromArray(nodes, ch_i) if ch_i< l and nodes[ch_i] != None else None
    return node

# Result checkers

def checkValue(correct, res):
    if correct == res:
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)

def checkList(correct, res):
    if len(correct) == len(res) and "".join(str(s) for s in correct) == "".join(str(s) for s in res):
        print("[v]", res)
    else:
        print(">>> INCORRECT >>>", correct, " | ", res)