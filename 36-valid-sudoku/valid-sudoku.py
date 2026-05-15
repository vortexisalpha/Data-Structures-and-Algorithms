class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def cond1():
            for i in range(len(board)):
                all_nums = set([str(i) for i in range(1,10)])
                for j in range(len(board[0])):
                    if board[i][j] == '.':
                        continue
                    elif board[i][j] not in all_nums:
                        return False
                    else:
                        all_nums.remove(board[i][j])
            return True

        def cond2():
            for j in range(len(board[0])):
                all_nums = set([str(i) for i in range(1,10)])
                for i in range(len(board)):
                    if board[i][j] == '.':
                        continue
                    elif board[i][j] not in all_nums:
                        return False
                    else:
                        all_nums.remove(board[i][j])
            return True

        def cond3():
            for x in range(3):
                for y in range(3):

                    all_nums = set([str(i) for i in range(1,10)])
                    for i in range(3):
                        for j in range(3):
                            if board[3*y + i][3*x + j] == '.':
                                continue
                            elif board[3*y + i][3*x + j] not in all_nums:
                                return False
                            else:
                                all_nums.remove(board[3*y + i][3*x + j])
            return True
        return cond1() and cond2() and cond3()