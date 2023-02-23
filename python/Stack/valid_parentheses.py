
def valid_parentheses(s: str) -> bool:
    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    stack = []

    for char in s:
        if char not in pairs:
            stack.append(char)
            continue
        if not stack or stack[-1] != pairs[char]:
            return False
        stack.pop()
    return not stack

