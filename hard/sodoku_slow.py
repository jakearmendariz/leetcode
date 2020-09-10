class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def solve_sodoku(board, i, j):
            if j >= self.n:
                i +=1
                j = 0
            if i >= self.n:
                # The board is finished
                return True
            if board[i][j] is '.':
                for value in range(1, self.n+1):
                    # print('Asserting value: ', value, 'on i:{}, j:{}'.format(i, j))
                    if isValid(board, str(value), i, j):
                        # print('is valid for ', value)
                        board[i][j] = str(value)
                        if(solve_sodoku(board, i, j+1)):
                            return True
                        board[i][j] = '.'
                return False
            return solve_sodoku(board, i, j+1)
    
        def isValid(board, value, i, j):
            if value in board[i]:
                return False
            if any(value==board[x][j] for x in range(self.n)):
                return False
            sqr = sqrt(self.n)
            ibox, jbox = i//sqr, j//sqr
            
            for idex in range(int(ibox*sqr), int((ibox+1)*sqr)):
                for jdex in range(int(jbox*sqr), int((jbox+1)*sqr)):
                    if(board[idex][jdex] == value):
                         return False
            return True


        self.n = len(board)
        print(solve_sodoku(board, 0, 0))
        # :)