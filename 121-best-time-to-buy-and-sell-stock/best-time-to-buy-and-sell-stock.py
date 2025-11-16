class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # 2 1 7 1 2
        # 1 -6 6 -1
        n = len(prices)
        diff =  [0]*(n-1)
        for i in range(1, n):
            diff[i-1] =  prices[i] - prices[i-1]

        m_p = 0
        idx = 0
        tm_p = 0
        while(idx < n-1):
            while(idx < n-1 and diff[idx] > 0):
                tm_p += diff[idx]
                idx+=1
                print(tm_p)
            
            m_p = max(tm_p, m_p)
            if idx >= n-1:
                break
            tm_p += diff[idx]
            if tm_p < 0:
                tm_p = 0
            idx+=1
        return m_p

            
        
    
        