class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for x in row:
                if x in seen and x != '.':
                    return False
                seen.add(x)

        for i in range(len(board[0])):
            seen = set()
            for j in range(len(board)):
                if board[j][i] in seen and board[j][i] != '.':
                    return False
                seen.add(board[j][i])
        
        col = [(0,0), (1,0), (2,0), (0,1), (1,1), (2,1), (0,2), (1,2), (2,2)]

        for i in range(0,9,3):
            for j in range(0,9,3):
                seen = set()
                for x,y in col:
                    if board[i+y][j+x] in seen and board[i+y][j+x] != '.':
                        
                        return False
                    seen.add(board[i+y][j+x])
        return True