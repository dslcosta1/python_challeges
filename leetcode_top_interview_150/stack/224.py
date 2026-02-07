class Solution:
    def calculate(self, s: str) -> int:
        stack = [0]
        result = 0
        n = len(s)
        s = s + ' '
        i = 0
        signal = +1
        curr_number = 0
        multiplier = 10
        for c in s:
            if not c.isdigit():
                x = stack.pop()
                stack.append(x + curr_number)
                curr_number = 0

            match c:
                case '-':
                    signal = -1
                case '+':
                    signal = +1
                case '(':
                    stack.append(signal)
                    stack.append(0)
                    signal = +1
                case ')':
                    x = stack.pop()
                    signal = stack.pop()
                    y = stack.pop()
                    stack.append(y + (signal * x))
                case ' ':
                    continue
                case _:
                    curr_number =  ((curr_number * multiplier) +  (signal * int(c)))
        return stack.pop()