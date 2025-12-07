class Solution:
    from functools import cache
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) > len(text2):
            return self.longestCommonSubsequence(text2,text1) # ensure text1 is less than or equal to text2
        #abcde
        #ace
        #action: take or skip
        #rules: we can only take if last_idx_taken (from other word) to end (of other word ) contains that character
        # we can only skip if idx < len(text1)
        #Vn = max(1+take, skip) 

        #input the smaller one into 
        @cache
        def dp(idx, last_idx_taken):
            #can we take?
            if idx >= len(text1):
                return 0
            cur_val = text1[idx]
            can_take = False
            new_last_idx = 0
            for i in range(last_idx_taken+1, len(text2)):
                if cur_val == text2[i]:
                    can_take = True
                    new_last_idx = i
                    break
            if can_take:
                take = dp(idx+1,new_last_idx)
                ret_val = take + 1
            else:
                ret_val = 0
            
            #can we skip?
            if idx < len(text1):
                skip = dp(idx+1, last_idx_taken)
            else:
                skip = 0

            return max(ret_val, skip)

        a = dp(0,-1)

        return a