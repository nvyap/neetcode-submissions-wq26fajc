class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        req = {i:[] for i in range(numCourses)}
        visit = set()
        for crs,pre in prerequisites:
            req[crs].append(pre)
        
        def dfs(crs):
            if crs in visit:
                return False
            if req[crs]==[]:
                return True
            visit.add(crs)
            for pre in req[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            req[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

        