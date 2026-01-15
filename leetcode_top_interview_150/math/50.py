# https://leetcode.com/problems/powx-n/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def myPow(self, x: float, n: int) -> float:
        

        if n == 0: return 1
        if n < 0:
            x = 1/x 
            n = -n

        i = 1
        values = {}
        values[i] = x
        while i < n:
            i *= 2
            if i > n:
                break 
            x = x*x
            values[i] = x
            print(i)
        
        if i == n: return x
        
        i = i //2
        j = i
        while j > 0 and i < n:
            if i +j <= n:
                i += j
                x = x * values[j]
            j = j//2
            print(j)
            if i == n:
                break

        return x