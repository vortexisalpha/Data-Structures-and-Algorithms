class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            print(f"processing {c}")
            if c == "]":
                popped = stack.pop()
                pop_str = ""
                while popped != "[":
                    pop_str = popped + pop_str
                    popped = stack.pop()
                print(f"popped_str {pop_str}")
                popped = stack.pop()
                pop_num = ""
                while popped.isnumeric():
                    pop_num = popped + pop_num
                    if stack:
                        popped = stack.pop()
                    else:
                        break
                if not popped.isnumeric(): stack.append(popped)
                print(f"popped_num {pop_num}")
                stack.append(pop_str * int(pop_num))
                print(f"stack is now: {stack}")
            else:
                stack.append(c)

            print(stack)
        return "".join(stack)
            

        
            