class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #using (y,x)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        m, n = len(matrix), len(matrix[0])

        def set_rc_zero(y, x, matrix):
            for dir_y, dir_x in directions:
                cur_y = y
                cur_x = x

                while( -1 < (cur_y + dir_y) and (cur_y + dir_y) < len(matrix) and -1 < (cur_x + dir_x) and (cur_x + dir_x) < len(matrix[0])):
                    cur_y += dir_y
                    cur_x += dir_x
                    print(cur_y, cur_x)
                    matrix[cur_y][cur_x] = 0
        
        zero_pos = []
        for y in range(m):
            for x in range(n):
                if matrix[y][x] == 0:
                    zero_pos.append((y,x))
        for y,x in zero_pos:
            set_rc_zero(y,x,matrix)

        return matrix

        