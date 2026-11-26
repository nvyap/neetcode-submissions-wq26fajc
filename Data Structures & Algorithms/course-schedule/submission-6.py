class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {i:[] for i in range(numCourses)}
        visit = set()


        for c,p in prerequisites:
            preq[c].append(p)
        
        def dfs(cur):
            if cur in visit:
                return False
            if preq[cur] == []:
                return True

            visit.add(cur)
            for i in preq[cur]:
                if not dfs(i):
                    return False
            preq[cur] = []
            visit.remove(cur)
            
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        