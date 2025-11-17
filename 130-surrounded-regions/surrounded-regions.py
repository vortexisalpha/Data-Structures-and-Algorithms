class Solution:
    def check_neighbours(self, y, x, board):
        left, right, down, right = "X", "X", "X", "X"
        if x > 0:
            if board[y][x-1] == "O" and (y,x-1) not in self.seen:
                self.q.append((y,x-1))

        if y > 0:
            if board[y-1][x] == "O" and (y-1, x) not in self.seen:
                self.q.append((y-1, x))


        if x < len(board[0]) - 1:
            if board[y][x+1] == "O" and (y,x+1) not in self.seen:
                self.q.append((y,x+1))

        if y < len(board) - 1:
            if board[y+1][x] == "O" and (y+1,x) not in self.seen:
                self.q.append((y+1,x))

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.q = collections.deque()
        self.seen = set()

        for i in range(len(board[0])):
            for j in range(len(board)):
                if board[j][i] == "O" and (i == 0 or j == 0 or i == len(board[0]) - 1 or j == len(board) - 1):
                    self.q.append((j,i))


        l = len(self.q)
        while(l>0):
            print(self.q)
            cur = self.q.popleft()
            self.seen.add(cur)
            self.check_neighbours(cur[0],cur[1], board)
            l = len(self.q)
            
        for i in range(len(board[0])):
            for j in range(len(board)):
                board[j][i] = "X"
        
        for y, x in self.seen:
            board[y][x] = "O"






         