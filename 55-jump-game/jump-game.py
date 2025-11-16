class Solution:
    
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        bmask = [1] + [0]*(n-1)

        for i in range(n):
            if (bmask[i] == 1):
                for j in range(min(nums[i]+1, n-i)):
                    bmask[j + i] = 1
            if bmask[n-1] == 1:
                return True       
        return False


