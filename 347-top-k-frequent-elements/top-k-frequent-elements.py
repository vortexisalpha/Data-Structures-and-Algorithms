from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        sol = sorted(list(cnt.items()), key = lambda x: x[1], reverse=True)
        return [sol[i][0] for i in range(k)]
        