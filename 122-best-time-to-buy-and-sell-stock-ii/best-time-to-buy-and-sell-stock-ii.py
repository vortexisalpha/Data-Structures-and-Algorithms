class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        min_price = float("inf")
        prof = 0
        idx = 1
        n = len(prices)
        while idx < n:
            tmi_p = -1
            tma_p = -1

            if idx == 1 and prices[idx-1] < prices[idx]:
                tmi_p = prices[0]
            while idx < n and prices[idx-1] >= prices[idx]:
                tmi_p = prices[idx]
                idx += 1
            
            while idx < n and prices[idx-1] < prices[idx]:
                tma_p = prices[idx]
                idx += 1
            print(tmi_p, tma_p)
            if tmi_p != -1 and tma_p != -1:
                prof += tma_p - tmi_p
        
        return prof

