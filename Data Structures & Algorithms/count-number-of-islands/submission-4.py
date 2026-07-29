class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #depth first search, see island and sink, no need to revisit, keep going and when see 1 sink respective island
        # necessity, dimension, direction
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1,0],[0,1], [0,-1]]

        def dfs(r,c):
            #base case
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == "0":
                return #return nothing and exit
            #sink
            grid[r][c] = "0"
            for dr,dc in directions:
                dfs(r+dr, c+dc) # if output wrong number check the incrementer

        #main traverse and count
        island = 0
        for r in range(rows):
            for c in range(cols):
                    #find island and sink
                    if grid[r][c] == "1":
                        dfs(r,c) # to do the sinking
                        island += 1 # add after sink
        return island
        
        