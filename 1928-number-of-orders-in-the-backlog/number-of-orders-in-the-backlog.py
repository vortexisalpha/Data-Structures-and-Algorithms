import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy = []
        sell = []

        for price, amount, order_type in orders:
            if order_type == 0:
                heapq.heappush_max(buy, [price, amount])
            else:
                heapq.heappush(sell, [price, amount])
            
            while len(buy) > 0 and len(sell) > 0 and buy[0][0] >= sell[0][0]:
                min_amt = min(buy[0][1], sell[0][1])
                buy[0][1] -= min_amt
                sell[0][1] -= min_amt

                if buy[0][1] == 0:
                    heapq.heappop_max(buy)
                elif sell[0][1] == 0:
                    heapq.heappop(sell)

                


            

        num_in_bl = 0 
        for i in range(len(buy)):
            _, amt = heapq.heappop_max(buy)
            num_in_bl += amt
            num_in_bl %= (pow(10,9) + 7)
            
        for i in range(len(sell)):
            _, amt = heapq.heappop(sell)
            num_in_bl += amt
            num_in_bl %= (pow(10,9) + 7)

        return num_in_bl




