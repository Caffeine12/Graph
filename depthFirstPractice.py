# def depthFirst(graph,source):
#     stack = [source]
#     while len(stack)>0:
#         current = stack.pop()
#         print(current)
#         for neighbor in graph[current]:
#             stack.append(neighbor)

# def depthFirst(graph,source):
#     print(source)    
#     for neighbor in graph[source]:
#         depthFirst(graph,neighbor)

def breadthFirst(graph,source):
    queue_custom = [source]
    while(len(queue_custom)>0):
        current= queue_custom.pop(0)
        print(current)
        for neighbor in graph[current]:
            queue_custom.append(neighbor)
            
graph ={
        'a':['b','c'],
        'b':['d'],
        'c':['e'],
        'd':['f'],
        'e':[],
        'f':[]
        }

source= 'a'

breadthFirst(graph,source)

#depthFirst(graph,source)