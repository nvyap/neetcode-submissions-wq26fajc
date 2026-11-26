class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols = len(heights),len(heights[0])
        pac = set()
        atl = set()
        res = []

        def dfs(r,c,prevh,visit):
            if r<0 or c<0 or r==rows or c==cols or heights[r][c]<prevh or (r,c) in visit:
                return
            visit.add((r,c))
            dfs(r+1,c,heights[r][c],visit)
            dfs(r-1,c,heights[r][c],visit)
            dfs(r,c+1,heights[r][c],visit)
            dfs(r,c-1,heights[r][c],visit)


        for c in range(cols):
            dfs(0,c,-1,pac)
            dfs(rows-1,c,-1,atl)

        for r in range(rows):
            dfs(r,0,-1,pac)
            dfs(r,cols-1,-1,atl)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res



        