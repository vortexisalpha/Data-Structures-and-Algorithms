class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_strs = s.split(' ')
        for i in range(len(split_strs)-1,-1,-1):
            if len(split_strs[i]) > 0:
                return len(split_strs[i])
        return 1