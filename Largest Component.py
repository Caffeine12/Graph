#Function to find largest component
def largestComponent(graph):
    visited=set() #This set will help not to visit same nodes again and prevent infinite loops
    max_count=0
    # For every key in the graph, neighbours are traveresed 
    for key in graph:        
        if key not in visited:
            if len(visited)>max_count:
                max_count=len(visited) # updates the max_count of any connected nodes 
            visited=set() #Reset the visit set for a new set of connected nodes
            iterateMax(key,graph,visited)

    if len(visited)>max_count: #This check the last iterated value for visit set
        max_count=len(visited)
    return max_count

# Recursively traverse the neighbours of a key of graph 
def iterateMax(key,graph,visited):
    visited.add(key)
    for neighbour in graph[key]:
        if neighbour not in visited:
            iterateMax(neighbour,graph,visited)



graph = {0:[8,1,5],
         1:[0],
         5:[0,8],
         8:[0,5],
         2:[3,4],
         3:[2,4],
         4:[3,2]
         }
    
max = largestComponent(graph)
print(max)