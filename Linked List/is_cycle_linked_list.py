class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Naive solution
class SolutionOne:
    def hasCycle(self, head):
        seen = set()
        curr = head
        while curr:
            seen.add(curr)
            curr = curr.next
            if curr in seen:
                return True
        return False


# Solution with two pointers
class SolutionTwo:
    def hasCycle(self, head):
        fast_pointer = head
        slow_pointer = head

        while fast_pointer and fast_pointer.next:
            slow_pointer, fast_pointer = slow_pointer.next, fast_pointer.next.next
            if fast_pointer is slow_pointer:
                return True
        return False