def hasPath(graph,src,dst):
    stack = [src]
    #flag = False
    while(len(stack)):
        current = stack.pop()
        if dst == current:
            #flag=True
            #break
            return True
        for neighbor in graph[current]:
            stack.append(neighbor)
    #return flag
    return False

graph = {'f':['g','i'],
         'g':['h'],
         'h':[],
         'i':['g','k'],
         'j':['i'],
         'k':[]}

print(hasPath(graph,'f','k'))