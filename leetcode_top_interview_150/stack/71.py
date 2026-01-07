# https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        dirs = path.split("/")
        stack = []
        for d in dirs:
            if d == '': continue

            if d == '..':
                if len(stack) > 0:
                    a = stack.pop()
            elif d != '.':
                stack.append(d)
        
        return '/'+ "/".join(stack)
