from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cntr = Counter(nums)
        return [x for x, y in cntr.items() if y == 2]
        