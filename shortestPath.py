#Undirected graph shortest path finding - iterative approach
def shortestPath(graph,src,dst):
    path_list = []
    distance = 0
    visited = set(src)
    path_list.append([src,distance])

    while(len(path_list)>0):
        current = path_list.pop(0)
        distance = current[1]+1
        for neighbour in graph[current[0]]:
            if neighbour==dst:
                return distance
            if neighbour not in visited:
                path_list.append([neighbour,distance])
                visited.add(neighbour)
    return None

graph = {'w':['x','v'],
         'x':['w','y'],
         'y':['x','z'],
         'v':['w','z'],
         'z':['y','v']}
src = 'w'
dst = 'x'
distance = shortestPath(graph,src,dst)
print(distance)
