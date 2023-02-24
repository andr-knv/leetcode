class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reorderList(self, head):
        slow_pointer = head
        fast_pointer = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        second_half = slow_pointer.next
        slow_pointer.next = None
        prev = None

        while second_half:
            temp_next = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp_next

        first_half = head
        second_half = prev

        while second_half:
            temp_first = first_half.next
            temp_second = second_half.next

            first_half.next = second_half
            second_half.next = temp_first

            first_half = temp_first
            second_half = temp_second
