graph = {0:[8,1,5],
         1:[0],
         5:[0,8],
         8:[0,5],
         2:[3,4],
         3:[2,4],
         4:[3,2]
         }

def connectedComponentCount(graph):
    visited = set()
    count=0
    for key in graph:
        if key not in visited:
            count +=1
            iterateNeighbours(key,graph,visited)
    return count

 
def iterateNeighbours(key,graph,visited):
    visited.add(key)
    for neighbour in graph[key]:
        if neighbour not in visited:
            iterateNeighbours(neighbour,graph,visited)



print(connectedComponentCount(graph))