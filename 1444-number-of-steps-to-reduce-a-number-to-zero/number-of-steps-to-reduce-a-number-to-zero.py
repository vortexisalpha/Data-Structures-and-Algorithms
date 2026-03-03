class Solution:
    def numberOfSteps(self, num: int) -> int:
        score = 0
        bin_num = str(bin(num))[2:]
        for bin_char in bin_num:
            if bin_char == '0':
                score += 1
            else:
                score += 2
        
        return score - 1


        