from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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