class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        t_s = set(['+','-','*','/'])
        def add(a,b):
            return a + b
        def sub(a,b):
            return a - b
        def times(a,b):
            return a*b
        def divide(a,b):
            return a/b # //?

        for x in tokens:
            if x not in t_s:
                stack.append(x)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if x == '+':
                    stack.append(add(a,b))
                elif x == '-':
                    stack.append(sub(a,b))
                elif x == '*':
                    stack.append(times(a,b))
                elif x == '/':
                    stack.append(divide(a,b))
        return int(stack.pop())