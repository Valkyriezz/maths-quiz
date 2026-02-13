class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def dfs(i,visited):
            visited[i]=True
            for neigh in adj[i]:
                if not visited[neigh]:
                    dfs(neigh,visited) 
        visited=[False]*n
        count=0
        adj={i:[] for i in range(n)}
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        for i in range(n):
            if not visited[i]:
                dfs(i,visited)
                count+=1
        # return count
        # connected componets pata chal gaya
        # find parents and count extra edges(dsu)
        parent=[i for i in range(n)]
        rank=[0]*n
        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]
        edges=0
        def union(x,y):
            nonlocal edges
            rootx=find(x)
            rooty=find(y)
            if rootx==rooty:
                edges+=1 #an extra edge found
            if rank[rootx]>rank[rooty]:
                parent[rooty]=parent[rootx]
            elif rank[rootx]<rank[rooty]:
                parent[rootx]=parent[rooty]
            else:
                parent[rootx]=rooty
                rank[rootx]+=1
            return edges
        for u,v in connections:
            union(u,v)
        if edges>=count-1:
            return count-1
        else:
            return -1
            
            

