class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_price = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                max_price = max(max_price, p-min_price)

        return max_price
    
        