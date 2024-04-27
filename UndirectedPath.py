def undirectedPath(edges,src,dst):
    graph = makeGraph(edges)
    print(graph)
    return hasPath(graph,src,dst)

def hasPath(graph, src, dst, visited=None):
    if visited is None:
        visited = set()

    if src not in visited:
        visited.add(src)
        if src == dst:
            return True
        for neighbor in graph[src]:
            if hasPath(graph, neighbor, dst, visited):
                return True
    return False

def makeGraph(edges):
    graph = {}
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]]=[edge[1]]
        else:
            graph[edge[0]].append(edge[1])
        
        if edge[1] not in graph:
            graph[edge[1]]=[edge[0]]
        else:
            graph[edge[1]].append(edge[0])
    return graph

    
edges = [['i','j'],['k','i'],['m','k'],['k','l'],['o','n']]

print(undirectedPath(edges,'i','n'))
