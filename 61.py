# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        dummy_head = ListNode()
        dummy_head.next = head
        tail = dummy_head
        length = 0

        while tail.next:
            tail = tail.next
            length += 1

        k_eff = k % length
        if k_eff == 0:
            return dummy_head.next

        tail.next = dummy_head.next
        new_tail = dummy_head
        for _ in range(length - k_eff):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head