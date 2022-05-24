
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        area = []
        count = 0
        row = len(grid)
        col = len(grid[0])
        
         
        def dfs(x,y):
            if grid[x][y]==1:
                grid[x][y]=0
                nonlocal count 
                count += 1
                if y-1 >=0 : dfs(x,y-1)
                if x-1 >=0 : dfs(x-1,y)
                if y+1 < col : dfs(x,y+1)
                if x+1 < row :dfs(x+1,y)
        
        for i in range(row):
            for j in range(col):
                
                if grid[i][j]==1:
                    dfs(i,j)
                    area.append(count)
                    count=0

          
    
        if len(area) == 0:
            return 0
        else:
            return max(area)
                    
                
                
                
                
                
                