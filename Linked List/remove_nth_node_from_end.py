class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow_ptr = dummy
        fast_ptr = head

        for _ in range(n):
            fast_ptr = fast_ptr.next
        
        while fast_ptr:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        
        slow_ptr.next = slow_ptr.next.next
        return dummy.next