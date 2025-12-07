class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        p_nums = range(1,n+1)
        ans = []
        def backtrack(cur_nums, start_idx):
            if len(cur_nums) == k:
                nonlocal ans
                ans.append(cur_nums[:])
                return
            
            for i in range(start_idx, len(p_nums)):
                cur_nums.append(p_nums[i])
                backtrack(cur_nums, i+1)
                cur_nums.pop()
        backtrack([], 0)

        return ans