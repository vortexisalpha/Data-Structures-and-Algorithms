class Solution:
    def dp(self, n, idx):
        if (n, idx) not in self.memo:
            cur = self.triangle[n][idx]
            left = self.dp(n+1, idx)
            right = self.dp(n+1, idx+1)

            self.memo[(n, idx)] = min(left + cur, right + cur)

        return self.memo[(n,idx)]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.memo = {}
        for i,n in enumerate(triangle[len(triangle)-1]):
            self.memo[(len(triangle)-1,i)] = n
        self.triangle = triangle
        return self.dp(0, 0)
