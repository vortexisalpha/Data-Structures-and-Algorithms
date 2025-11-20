class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        for k,i in d.items():
            if i < 3:
                return k