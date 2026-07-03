class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch in "+-*/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                ans = 0
                if ch == '+':
                    ans = num1 + num2
                elif ch == '*':
                    ans = num1 * num2
                elif ch == '-':
                    ans = num2 - num1
                else:
                    ans = math.trunc(num2 / num1)
                stack.append(str(ans))
            else:
                stack.append(ch)
        return int(stack[0])