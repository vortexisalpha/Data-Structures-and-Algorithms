class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = collections.Counter(nums)
        return max(dic.keys(), key=dic.get)