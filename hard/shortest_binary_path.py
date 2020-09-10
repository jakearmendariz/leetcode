class Solution:
    # BFS
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        queue = []
        i=j=0
        queue.append([i,j])
        visited = [[False] * len(grid) for _ in range(len(grid))]
        steps = 0
        visited[i][j] = True
        while(len(queue) > 0):
            length = len(queue)
            while(length > 0):
                arr = queue.pop(0)
                i,j = arr[0], arr[1]

                if i == len(grid)-1 and i == j:
                    return steps+1
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid):
                            if grid[x][y] == 0 and not visited[x][y]:
                                queue.append([x, y])
                                visited[x][y] = True
                length -=1
            steps +=1
            
        return -1    
            