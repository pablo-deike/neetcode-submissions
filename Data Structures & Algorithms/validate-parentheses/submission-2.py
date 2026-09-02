class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        stack = []
        parenthesis_mapping = {
            "[": "]",
            "{": "}",
            "(": ")",
        }
        for c in s:
            if c in parenthesis_mapping.keys():
                stack.append(c)
                continue
            elif len(stack) == 0:
                return False
            elif parenthesis_mapping.get(stack[-1]) != c:
                return False
            stack.pop()
        return len(stack) == 0