class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        seen = []
        def backtrack(remainder, comb, start_idx):
            if remainder == 0:

                ans.append(comb[:])
                return
            if remainder < 0:
                return

            for i in range(start_idx, len(candidates)):
                comb.append(candidates[i])
                backtrack(remainder - candidates[i], comb, i)
                comb.pop()

        
        backtrack(target, [], 0)
        return ans