class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visit = set()

        hm = {i:[] for i in range(n)}

        for k,j in edges:
            hm[k].append(j)
            hm[j].append(k)

        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for neighbor in hm[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visit) == n