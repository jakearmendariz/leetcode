class Solution:
    # BFS
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        visited = [0] *N
        count = 0
        queue = []
        
        arr = [i for i in range(N)]
        # print(arr)
        while(len(arr) > 0):
            queue.append(arr.pop(0))  
            while len(queue) > 0:
                i = queue.pop(0)
                if visited[i] == 0:
                    count +=1
                    # print('setting: i:',i, 'to visited')
                    visited[i] = 1
                    #Notify all neighbors that they have been visited
                for j, value in enumerate(M[i]):
                    # print('checking:',i, j)
                    if value == 1 and visited[j] == 0:
                        # print('setting: j:',j, 'to visited')
                        visited[j] = 1
                        queue.append(j)
                        arr.remove(j)
                if i in arr:
                    arr.remove(i)
            
        return count