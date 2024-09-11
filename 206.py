# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        cur = head

        while cur:
            next = cur.next
            cur.next = dummy_head.next
            dummy_head.next = cur
            cur = next

        return dummy_head.next