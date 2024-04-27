graph = {0:[8,1,5],
         1:[0],
         5:[0,8],
         8:[0,5],
         2:[3,4],
         3:[2,4],
         4:[3,2]
         }

def connectedComponentCount(graph):
    value_list = []
    for sublist in graph.values():
        for value in sublist:
            value_list.append(value)
    unique_sorted_list = sorted(set(value_list))
    print(unique_sorted_list)

    visited = set()
    count = 0
    stack=[]

    for item in unique_sorted_list:





        # if item not in visited:
        #     stack.append(item)
        #     count+=1
        #     while(len(stack)>0):
        #         current = stack.pop()
        #         visited.add(current)
        #         for neighbour in graph[current]:
        #             if neighbour not in visited:
        #                 stack.append(neighbour)
    return count



print(connectedComponentCount(graph))