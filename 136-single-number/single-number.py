class Solution:
    from collections import Counter
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i, x in count.items():
            if x == 1:
                return i