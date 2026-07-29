class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #base necessity
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r,c): #defining bfs and obiously what you pass in
            q= [] #double ended queue
            visit.add((r,c)) #after visiting (r,c) adding it to a queue to be checked for neighbors
            q.append((r,c))
            while q: #when there is still land to be checked
                row, col = q.pop(0) #remove from queue and do job, this is different from rows cols and is defining the r,c two values in the queue
                directions = [[1,0], [-1,0], [0,1],[0,-1]] #adding the directions that need to be checked after deleting its starting point and new locations become starting
                for dr, dc in directions:
                    r,c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))


        #marking mechanism, use bfs before define
        for r in range(rows): #r and c are numbers and therefore not iterable, have to use range()
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c) #using bfs passing in r and c
                    islands += 1
        return islands



        