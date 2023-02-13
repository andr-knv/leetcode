class SolutionOne:


    def valid_parentheses(s: str) -> bool:
        stack = []
        OPENING_BRACES = '([{'
        CLOSING_BRACES = ')]}'
        
        for val in s:
            if val in OPENING_BRACES:
                stack.append(val)
            if val in CLOSING_BRACES and not stack:
                return False
            if val in CLOSING_BRACES:
                opening_from_stack = stack.pop()
                if opening_from_stack == '(' and val != ')' \
                    or opening_from_stack == '{' and val != '}' \
                        or opening_from_stack == '[' and val != ']':
                    return False
        return not stack


class SolutionTwo:


    def valid_parentheses(s: str) -> bool:
        stack = []
        PAIRS = {
            "{": "}",
            "[": "]",
            "(": ")",}
        OPENING_BRACES = '{[('
        CLOSING_BRACES = ')}]'
    
        for val in s:
            if val in OPENING_BRACES:
                stack.append(val)
            elif val in CLOSING_BRACES:
                if not stack:
                    return False
                if PAIRS[stack.pop()] != val:
                    return False
        return not stack


