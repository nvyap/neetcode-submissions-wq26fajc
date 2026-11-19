class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid), len(grid[0])
        islands = 0
        path = set()

        def dfs(r,c,path):
            if r<0 or c<0 or r==rows or c==cols or grid[r][c]!="1" or (r,c) in path:
                return 
            path.add((r,c))
            dfs(r+1,c,path)
            dfs(r-1,c,path)
            dfs(r,c+1,path)
            dfs(r,c-1,path)
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in path:
                    dfs(r,c,path)
                    islands += 1
        return islands
        