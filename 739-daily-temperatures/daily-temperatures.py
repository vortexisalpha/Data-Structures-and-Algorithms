class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        m_stack = collections.deque() #decresing only
        arr = [0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            if len(m_stack) == 0:
                m_stack.append([temp,i])
            elif m_stack[-1][0] >= temp:
                m_stack.append([temp,i])
            else:
                while(len(m_stack) != 0):
                    top_temp = m_stack[-1][0]
                    idx = m_stack[-1][1]
                    if top_temp < temp:
                        m_stack.pop()
                        arr[idx] = i - idx
                    else:
                        break
                m_stack.append([temp,i])
                
        return arr