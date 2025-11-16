class Solution:
    
    def dp(self, n, nums, memo):
        if n == 0:
            return 0

        if n not in memo:
            p_pos = []
            for i in range(n):
                if nums[i] + i >= n:
                    p_pos.append(i)

            if n > 1 and p_pos == []: # >=?
                return float("inf")
            
            memo[n] = float("inf")
            for pos in p_pos:
                memo[n] = min(memo[n],1 + self.dp(pos, nums, memo))
            

        return memo[n]

    def jump(self, nums: List[int]) -> int:
        """
        [2,3,1,1,4]
        start at 4 -> explore idxs 3, 1
        dp[4] = min(1+dp[3],1+dp[1])
        dp[3]  = min(1+dp[2])
        if n > 1 and explore is empty return infinity
        if n == 1 return 
        """
        memo = {}
    
        return self.dp(len(nums)-1,nums,memo)