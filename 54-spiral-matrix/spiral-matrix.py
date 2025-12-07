class Solution:
    from collections import deque
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir_map = {(0,1): (1,0), (1,0): (0,-1), (0, -1): (-1, 0), (-1,0): (0,1)} # y x

        y = 0
        x = 0
        ans = []
        def bfs(y,x):
            nonlocal ans
            seen = set()
            coord_q = deque()
            cur_dir = (0,1)
            coord_q.append((y,x))

            while(len(coord_q) > 0):
                cur_y, cur_x = coord_q.pop()
                print(cur_y, cur_x)
                ans.append(matrix[cur_y][cur_x])

                seen.add((cur_y, cur_x))
                
                dir_y, dir_x = cur_dir
                #if the coord in the direction we are going is in range and hasnt been touched yet
                if (dir_y + cur_y, dir_x + cur_x) not in seen and 0 <= (dir_y + cur_y) and  (dir_y + cur_y) < len(matrix) and 0 <= (dir_x + cur_x) and  (dir_x + cur_x) < len(matrix[0]):
                    coord_q.append((dir_y + cur_y, dir_x + cur_x))
                else:
                    cur_dir = dir_map[cur_dir]
                    dir_y, dir_x = cur_dir
                    if (dir_y + cur_y, dir_x + cur_x) not in seen and 0 <= (dir_y + cur_y) and  (dir_y + cur_y) < len(matrix) and 0 <= (dir_x + cur_x) and  (dir_x + cur_x) < len(matrix[0]):
                        coord_q.append((dir_y + cur_y, dir_x + cur_x))
        
        bfs(0,0)
        return ans


