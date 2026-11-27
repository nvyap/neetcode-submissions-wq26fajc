class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {i:[] for i in range(numCourses)}
        visit = set()
        for c, p in prerequisites:
            preq[c].append(p)
        
        def dfs(crs):
            if crs in visit:
                return False
            
            if preq[crs] == []:
                return True
            visit.add(crs)
            for c in preq[crs]:
                if not dfs(c): return False
            
            preq[crs] = []
            visit.remove(crs)
            
            return True
        
        for cr in range(numCourses):
            if not dfs(cr): return False
        return True
        