class Solution:
    from functools import cache
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        ans = -1e9
        adj = [[] for i in range(n)]
        for nd, ch, we in edges:
            adj[nd].append((ch, we))

        @cache
        def dp(steps_rem, node, cur_sum):
            if cur_sum >= t:
                return 
            
            if steps_rem == 0:
                nonlocal ans
                ans =  max(cur_sum,ans)
                return
            
            res = 0
            for child, weight in adj[node]:
                dp(steps_rem-1, child, cur_sum + weight)
                           
        for i in range(n):
            dp(k,i,0)
        return ans if ans != -1e9 else -1