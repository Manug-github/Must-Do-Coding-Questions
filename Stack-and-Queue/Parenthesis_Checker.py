def parenthesis_checker(s):
    """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Time Complexity O(n)
    Space Complexity O(n)
    """
    d = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if stack and char in d:
            last = stack.pop()
            if last != d[char]:
                return False
        else:
            stack.append(char)
    if stack:
        return False
    return True
