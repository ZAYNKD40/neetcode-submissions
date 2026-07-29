class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #necessity
        #get dimensions
        rows, cols = len(grid), len(grid[0])
        visit = set()
        #visit set dont want dfs to rerun and recount the same square
        #dfs
        def dfs(r,c):
            #base case for recursion
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r,c) in visit:
                return 0
            visit.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        #main 
        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r,c))
        
        return area
        