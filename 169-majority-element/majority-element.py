class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        size = len(nums)
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1

        for k,v in dic.items():
            if size//2 < v:
                return k