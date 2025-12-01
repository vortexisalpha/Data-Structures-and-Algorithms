class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        h = 0
        for i in range(len(citations)):
            h = max(h,min(citations[i],i+1))
        return h
        