class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        preq = {i:[] for i in range(n)}
        visit = set()

        for s,d in edges:
            preq[s].append(d)
            preq[d].append(s)
        
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for neighbor in preq[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        return dfs(0, -1) and len(visit)==n
        