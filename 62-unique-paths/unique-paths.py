class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # prev=[0]*n
        # for i in range(m):
        #     temp=[0]*n
        #     for j in range(n):
        #         if i==0 and j==0:
        #             temp[j]=1
        #         else:
        #             if i>0:
        #                 up=prev[j]  
        #             else:
        #                 up=0
        #             if j>0:
        #                 left=temp[j-1]
        #             else: 
        #                 left=0
        #             temp[j]=up+left
        #     prev=temp
        # return prev[n-1]
        dp=[[-1]*n for i in range(m)]
        def f(i,j):
            if i>m or j>n:
                return 0
            if i==m-1 or j==n-1:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j] = f(i+1,j)+f(i,j+1)
            return dp[i][j]
        return f(0,0)