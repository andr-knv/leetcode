const reverseList = function (head) {
  let previous = null;
  let current = head;

  while (current) {
    _next = current.next;
    current.next = previous;
    previous = current;
    current = _next;
  }
  return previous;
};
