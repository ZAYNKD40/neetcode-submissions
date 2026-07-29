class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        YorN = {'}': '{', "]": "[", ")" : "("}

        for c in s:
            if c in YorN: #check against KEY, so if closing then be the pop checker
                if stack and stack[-1] == YorN[c]:
                    stack.pop()
                else:
                    return False
            else: # if not closing and opening instead move to stack to wait to be matched and potentially cancelled
                stack.append(c)
        return True if not stack else False

        