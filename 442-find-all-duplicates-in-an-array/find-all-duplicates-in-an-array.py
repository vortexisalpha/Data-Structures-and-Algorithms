class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for num in nums:
            nums[abs(num)-1] = -nums[abs(num)-1]
        sol = []
        for num in nums:
            if nums[abs(num)-1] > 0:
                sol.append(abs(num))
                nums[abs(num) - 1] = -nums[abs(num) - 1]
        return sol
        