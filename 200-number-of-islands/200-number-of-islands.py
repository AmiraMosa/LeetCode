class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        row =len(grid)
        col = len(grid[0])
        num_of_islands = 0
        
        
        def dfs(x,y):
            
            if grid[x][y] == '1':
                grid[x][y] = '0'
                if y-1 >=0 : dfs(x,y-1)
                if x-1 >=0 : dfs(x-1,y)
                if y+1 < col : dfs(x,y+1)
                if x+1 < row :dfs(x+1,y)
                    
    
        
        for i in range(row):
            for j in range(col):
                
                if grid[i][j] == '1':
                    dfs(i,j)
                    num_of_islands+=1
                    
                    
        return num_of_islands
                    
                
                
            
        