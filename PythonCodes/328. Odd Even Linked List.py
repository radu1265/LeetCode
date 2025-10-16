# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        even_head = head.next
        even_first = head.next
        odd_head = head
        odd_prev = head

        while odd_head and odd_head.next:
            odd_head.next = odd_head.next.next
            n_o = odd_head
            odd_head = odd_head.next
            if even_head and even_head.next:
                even_head.next = even_head.next.next
                even_head = even_head.next
        if odd_head:
            odd_head.next = n_e
        else: n_o.next = n_e
        return head
        
