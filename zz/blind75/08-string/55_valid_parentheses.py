# 55. Valid Parentheses — a closer must match the top of the stack
# Run: python 55_valid_parentheses.py
# Time: O(n). Space: O(n).



def isValid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack



print(isValid("()[]{}"))
print(isValid("(]"))
