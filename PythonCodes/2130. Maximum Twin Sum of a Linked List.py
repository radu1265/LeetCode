# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self, middle: Optional[ListNode]) -> Optional[ListNode]:
        curr = middle
        head = middle
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        
    def pairSum(self, head: Optional[ListNode]) -> int:
        middle, end = head, head
        start = head
        max_sum = 0
        while end and end.next:
            middle = middle.next
            end = end.next.next

        rev_second_half = self.reverseLinkedList(middle)
        while rev_second_half:
            max_sum = max(max_sum, start.val + rev_second_half.val)
            start = start.next
            rev_second_half = rev_second_half.next
        return max_sum
