# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        toggle = True
        dummy_head = ListNode()
        cur = dummy_head
        
        while head and prev:
            if toggle:
                cur.next = head
                head = head.next
            else:
                cur.next = prev
                prev = prev.next
            toggle = not toggle
            cur = cur.next

        cur.next = head if head else prev

        head = dummy_head.next