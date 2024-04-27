def depthFirstPrint(graph, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
                stack.append(neighbor)

source='a'
graph = {
    'a':['b','c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}
depthFirstPrint(graph, source)