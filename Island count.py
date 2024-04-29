def countIsland(grid):

    #TODO: 1. Find the length of row and column
    rows = len(grid)
    columns = len(grid[0])
    visited = set()
    islandNumber=0

    #TODO: 2. Run two nested loops to traverse the grid
    for row in range(0,rows):
        for column in range(0,columns):

            #TODO: 3. Check the row column tuple, is it visited already?
            if (row,column) not in visited:

                #Make the (row,colummn) tuples visited
                visited.add((row,column))

                #TODO: 4. Check the value of that particular grid position.Is it Land ?
                if grid[row][column]=='L':
                    islandNumber+=1

                    #TODO: 5. Find the adjacent lands and make the particular grid positions visited
                    findAdjacentLands(grid,row,column,visited)
    return islandNumber

            
            



def findAdjacentLands(grid,row,column,visited):
    if column-1>=0:
        if (row,column-1) not in visited:
            visited.add((row,column-1))
            if grid[row][column-1]=='L':
                findAdjacentLands(grid,row,column-1,visited)
    
    if column+1<len(grid[0]):
        if (row,column+1) not in visited:
            visited.add((row,column+1))
            if grid[row][column+1]=='L':
                findAdjacentLands(grid,row,column+1,visited)

    if row-1>=0:
        if (row-1,column) not in visited:
            visited.add((row-1,column))
            if grid[row-1][column]=='L':
                findAdjacentLands(grid,row-1,column,visited)
    
    if row+1<len(grid):
        if (row+1,column) not in visited:
            visited.add((row+1,column))
            if grid[row+1][column]=='L':
                findAdjacentLands(grid,row+1,column,visited)




grid =[['W','L','W','W','W'],
       ['W','L','W','W','W'],
       ['W','W','W','L','W'],
       ['W','W','L','L','W'],
       ['L','W','W','L','L'],
       ['L','L','W','W','W']]

islandNumber=countIsland(grid)
print(islandNumber)