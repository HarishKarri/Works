# 200. Number of Islands
# Medium

# 10167

# 267

# Add to List

# Share
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == '1'):
                    count +=1
                    self.checkingIslands(grid,i,j)
        return count
    
    def checkingIslands(self,grid,x,y):
        if(x<0 or y<0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == "0"):
            return
        else:
            grid[x][y]= "0"
        self.checkingIslands(grid, x+1,y)
        self.checkingIslands(grid, x-1,y)
        self.checkingIslands(grid, x,y+1)
        self.checkingIslands(grid, x,y-1)   