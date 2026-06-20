class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS,COLS = len(heights),len(heights[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c,pacific,atlantic,val,visitor):
            val = heights[r][c]
            if(r<0 or c<0 or r>ROWS-1 or c>COLS-1 or visitor[r][c]==1):
                return pacific,atlantic
            visitor[r][c] = 1
            for dr,dc in directions:
                newRC,newCC = r+dr,c+dc
                if(newRC<0 or newCC<0):
                    pacific = 1
                if(newRC>ROWS-1 or newCC>COLS-1):
                    atlantic = 1
                if(newRC>=0 and newCC>=0 and newRC<=ROWS-1 and newCC<=COLS-1 and val>=heights[newRC][newCC]):    
                    pacific,atlantic = dfs(newRC,newCC,pacific,atlantic,val,visitor)
            return pacific,atlantic 

        for r in range(ROWS):
            for c in range(COLS):
                pacific = 0
                atlantic = 0
                val = heights[r][c]
                visitor = [[0 for i in range(COLS)] for i in range(ROWS)]
                pacific,atlantic = dfs(r,c,pacific,atlantic,val,visitor)
                if pacific==1 and atlantic==1:
                    res.append([r,c])
        return res            

             


