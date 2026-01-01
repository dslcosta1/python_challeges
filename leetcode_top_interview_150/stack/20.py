class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '{':'}',
            '(':')',
            '[':']'
        }

        for c in s:
            if c == '{' or c == '[' or c == '(':
                stack.append(c)
            else:
                if len(stack) <= 0: return False
                
                last = stack.pop()
                pair = pairs.get(last, '#')

                if pair != c: return False
    
        return len(stack) == 0 