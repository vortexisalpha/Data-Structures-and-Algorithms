class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s = sum(int(x) for x in list(str(nums[i])))
            if s == i:
                return i
        return -1