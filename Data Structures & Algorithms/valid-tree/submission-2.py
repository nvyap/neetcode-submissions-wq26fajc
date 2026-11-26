class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph_hm = {i:[] for i in range(n)}
        visit = set()
        for c,p in edges:
            graph_hm[c].append(p)
            graph_hm[p].append(c)
        
        def dfs(cur,prev):
            if cur in visit:
                return False
            visit.add(cur)
            for c in graph_hm[cur]:
                if prev==c:
                    continue
                
                if not dfs(c,cur):
                    return False
                #visit.remove(c)
            return True
        
        return dfs(0,-1) and len(visit)==n
        