class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n==0:
            return True
        pre = {i:[] for i in range(n)}  
        visit = set()

        for j,k in edges:
            pre[j].append(k)
            pre[k].append(j)
        
        def dfs(n,p):
            if n in visit:
                return False
            visit.add(n)
            for nei in pre[n]:
                if nei == p:
                    continue
                if not dfs(nei,n):
                    return False
            return True
        
        return dfs(0,-1) and len(visit)==n
        