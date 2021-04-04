# 234. Palindrome Linked List

# Easy

# Given the head of a singly linked list, return true if it is a
# palindrome.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false


# Constraints:
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9

# Follow up: Could you do it in O(n) time and O(1) space?

from utils import ListNode, checkValue, listFromArray, listToArray


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        if l < 2:
            return True
        mid = l // 2 + l % 2
        i, l_tail = 1, head
        while i < mid:
            i, l_tail = i + 1, l_tail.next

        r_head, p = None, l_tail.next
        while p:
            n = p.next
            p.next = r_head
            r_head = p
            p = n

        l_tail.next = r_head
        p, q = head, r_head
        while q:
            if p.val != q.val:
                return False
            p, q = p.next, q.next
        return True


t = Solution()

checkValue(True, t.isPalindrome(listFromArray([2, 2])))
checkValue(True, t.isPalindrome(listFromArray([1, 2, 3, 2, 1])))
checkValue(True, t.isPalindrome(listFromArray([1, 2, 3, 4, 4, 3, 2, 1])))
checkValue(False, t.isPalindrome(listFromArray([2, 1])))
checkValue(False, t.isPalindrome(listFromArray([1, 2, 3, 1, 2])))
checkValue(False, t.isPalindrome(listFromArray([1, 2, 3, 4, 4, 3, 4, 1])))
