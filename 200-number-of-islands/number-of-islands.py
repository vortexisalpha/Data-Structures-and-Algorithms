class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0), (-1,0),(0,-1), (0,1)]

        def bfs(x,y,island_num):
            nonlocal grid
            seen = set()
            island_q = deque()

            island_q.append((y,x))

            while(len(island_q) > 0):
                cur_y, cur_x = island_q.pop()   
                seen.add((cur_y, cur_x))
                
                grid[cur_y][cur_x] = str(island_num)

                for iy, ix in directions:
                    if 0 <= (iy + cur_y) and (iy + cur_y) < len(grid) and 0 <= (ix + cur_x) and (ix + cur_x) < len(grid[0]):
                        if (grid[iy + cur_y][ix + cur_x] == "1"): island_q.append((iy + cur_y, ix + cur_x))
        
        island_count = 2
        for y_it in range(len(grid)):
            for x_it in range(len(grid[0])):
                if grid[y_it][x_it] == "1":
                    bfs(x_it, y_it, island_count)
                    island_count+=1
        island_count -= 2

        return island_count
