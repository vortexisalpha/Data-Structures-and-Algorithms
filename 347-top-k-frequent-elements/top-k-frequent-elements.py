from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        return heapq.nlargest(k, cnt.keys(), key=cnt.get)
        