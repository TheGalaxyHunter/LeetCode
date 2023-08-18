class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False

        stack = []
        brackets= {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for char in s:
            if char in brackets:
                stack.append(char)
                continue

            elif not stack or char != brackets[stack.pop()]:
                return False

        return False if stack else True