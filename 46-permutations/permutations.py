class Solution:
    def pm(self, nums)-> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        perms = []
        for i in range(len(nums)):
            t_l = nums[:i] + nums[i+1:]
            #print(t_l)
            pms = self.pm(t_l)
            for p in pms:
                perms.append([nums[i]] + p)

        return perms
    def permute(self, nums: List[int]) -> List[List[int]]:
        a = self.pm(nums)
        return a
        
        

