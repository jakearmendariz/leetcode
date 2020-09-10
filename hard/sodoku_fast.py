class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rowsol = [set(str(i) for i in range(1,10)) for _ in range(9) ]
        colsol = [set(str(i) for i in range(1,10)) for _ in range(9) ]
        boxsol = [[set(str(i) for i in range(1,10)) for _ in range(3) ] for _ in range(3) ]
        for row in range(9):
            for col in range(9):
                if board[row][col] in rowsol[row]: rowsol[row].remove(board[row][col])
                if board[row][col] in colsol[col]: colsol[col].remove(board[row][col])
                if board[row][col] in boxsol[row//3][col//3]:
                    boxsol[row//3][col//3].remove(board[row][col])
    
    # use a minheap to maintain a todo list. do the least option item first
        todo = []
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    sol = rowsol[row].intersection(colsol[col]).intersection(
                        boxsol[row//3][col//3])
                    todo.append([len(sol),(row,col)])
    
        import heapq
        heapq.heapify(todo)
        def guess():# n = [0,81)
            if not todo: return True
            _,(row,col) = heapq.heappop(todo)
            sol = rowsol[row].intersection(colsol[col]).intersection(boxsol[row//3][col//3])
            for ans in sol:
                board[row][col] = ans
                rowsol[row].remove(ans)
                colsol[col].remove(ans)
                boxsol[row//3][col//3].remove(ans)
                succeed = guess() # continue to guess the next cell
                if succeed: return True
                else:
                    rowsol[row].add(ans)
                    colsol[col].add(ans)
                    boxsol[row//3][col//3].add(ans)
                    board[row][col] = '.'
            heapq.heappush(todo,[len(sol),(row,col)] ) 
            return False
        guess()
        