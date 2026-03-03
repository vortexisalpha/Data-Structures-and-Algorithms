class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        end_str = ""
        done_once = False
        for i in range(len(num_str)):
            if num_str[i] == '6' and not done_once:
                end_str += '9'
                done_once = True
            else:
                end_str += num_str[i]
        return int(end_str)
            

        