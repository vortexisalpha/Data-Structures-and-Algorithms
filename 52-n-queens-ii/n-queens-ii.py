class Solution:
    def totalNQueens(self, n: int) -> int:

       
    
        grid = [[0]*n for i in range(n)]

        solutions = 0

        def num_locations_available(grid):
            locos = []
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == 0:
                        locos.append((y,x))
            return locos
        
        def place_queens(grid, location, repl):
            y,x = location
            grid[y][x] = repl
            dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
            for dir in dirs:
                cur_y = y
                cur_x = x
                
                dir_y, dir_x = dir
                while -1< dir_y + cur_y and dir_y + cur_y < len(grid) and -1 < dir_x + cur_x and dir_x + cur_x < len(grid[0]):
                    grid[dir_y + cur_y][dir_x + cur_x] = repl
                    cur_y = dir_y + cur_y
                    cur_x = dir_x + cur_x

        #store locations as (y,x)
        def backtrack(grid, nqueens):
            for a in grid:
                print(a)
            print()
            num_available = num_locations_available(grid)
            if len(num_available) < n-nqueens:
                return
            if nqueens == n:
                nonlocal solutions
                solutions+=1
                return

            for location in num_available:
                if location[0] == nqueens:
                    preserved_grid = [grid[i][:] for i in range(len(grid))]
                    place_queens(grid, location, 1)
                    backtrack(grid, nqueens+1)
                    grid = preserved_grid

        
        backtrack(grid, 0)

        return solutions

