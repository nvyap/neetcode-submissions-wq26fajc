class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq_hm = {i:[] for i in range(numCourses)}
        visit = set()

        for course, prereq in prerequisites:
            preq_hm[course].append(prereq)
        
        def dfs(crs):
            if crs in visit:
                return False
            if preq_hm[crs] == []:
                return True
            visit.add(crs)
            for c in preq_hm[crs]:
                if not dfs(c):
                    return False
            preq_hm[crs] = []
            visit.remove(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            


        