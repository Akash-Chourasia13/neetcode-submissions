class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandNum = 0
        visitor = [["0" for _ in range(len(grid[0]))] for _ in range(len(grid))]
        nearByLand = [(0,1),(-1,0),(1,0),(0,-1)]
        # visiting the each index in grid to check if the land starts
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == "1" and visitor[i][j] == "0":
                    visitor[i][j] = "1"
                    islandNum += 1
                    visitor = self.connectingLands(grid,i,j,visitor,nearByLand)
        return islandNum
    def connectingLands(self,grid,i,j,visitor,nearByLand):
        if grid[i][j] == "0":
            return visitor
        visitor[i][j] = "1" 
        for _ in(nearByLand):
            if ((i+_[0]>=0 and i+_[0]<=(len(grid)-1)) and (j+_[1]>=0 and j+_[1]<=(len(grid[0])-1)) and visitor[i+_[0]][j+_[1]]=="0"):
                visitor = self.connectingLands(grid,i+_[0],j+_[1],visitor,nearByLand)
        return visitor

        