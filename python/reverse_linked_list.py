def reverse_list(head):
    previous = None
    current = head

    while current:
        _next = current.next
        current.next = previous
        previous = current
        current = _next
    return previous

