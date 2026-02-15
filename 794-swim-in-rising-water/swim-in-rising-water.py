class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minheap=[]
        n=len(grid)
        visited=[[False]*n for i in range(n)]
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        heapq.heappush(minheap,(grid[0][0],0,0))
        while minheap:
            point,row,col=heapq.heappop(minheap)
            if visited[row][col]==True:
                continue
            visited[row][col]=True
            if row==n-1 and col==n-1:
                return point
            for x,y in directions:
                nx=row+x
                ny=col+y
                if 0<=nx<n and 0<=ny<n:
                    if visited[nx][ny]==False:
                        heapq.heappush(minheap,(max(point,grid[nx][ny]),nx,ny))