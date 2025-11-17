class Solution:
    def dp(self, x, y):
        if (x,y) not in self.memo:
            right = float("inf")
            down = float("inf")

            if x > 1:
                right = self.dp(x-1,y)
            if y > 1:
                down = self.dp(x,y-1)

            cur_sqr =  self.grid[self.m-y][self.n-x]
            self.memo[(x,y)] = min(down + cur_sqr, right + cur_sqr)
        return self.memo[(x,y)]

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.n = len(grid[0])
        self.m = len(grid)
        self.memo = {(1,1): grid[self.m-1][self.n-1]}

        return self.dp(self.n,self.m)
        