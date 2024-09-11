# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k):
            prev, cur = None, head
            for _ in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            return prev

        node = head
        counts = 0

        while node and counts < k:
            node = node.next
            counts += 1

        if counts == k:
            reversed_head = reverse(head, k)
            head.next = self.reverseKGroup(node, k)

            return reversed_head

        return head

