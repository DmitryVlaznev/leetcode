# 142. Linked List Cycle II

# Given a linked list, return the node where the cycle begins. If there
# is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list
# that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's
# next pointer is connected to. Note that pos is not passed as a
# parameter.

# Notice that you should not modify the linked list.

# Follow up:

# Can you solve it using O(1) (i.e. constant) memory?

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1

# Explanation: There is a cycle in the linked list, where tail connects
# to the second node.

# Example 2:
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects
# to the first node.

# Example 3:
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.

# Constraints:
# * The number of the nodes in the list is in the range [0, 104].
# * -105 <= Node.val <= 105
# * pos is -1 or a valid index in the linked-list.


from utils import ListNode, checkValue, listFromArray


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        slow = head.next
        if slow is None:
            return None

        fast = head.next.next
        if fast is None:
            return None

        while slow != fast:
            slow = slow.next
            if fast.next is None or fast.next.next is None:
                return None
            fast = fast.next.next

        fast = head
        res = 0

        while slow != fast:
            slow = slow.next
            fast = fast.next
            res += 1
        return res


t = Solution()
head = listFromArray([3, 2, 0, -4])
head.next.next.next.next = head.next

checkValue(1, t.detectCycle(head))