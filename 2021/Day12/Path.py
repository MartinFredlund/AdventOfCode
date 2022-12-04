
def nextPath(cur, route):
    global amountRoute
    for des in graph[cur]:
        if(des == "end"):
            amountRoute += 1
            endRoute = []
            endRoute += route
            endRoute.append(cur)
            endRoute.append("end")
            print("End", endRoute)
        elif(not (des in route) or des.isupper()):
            newRoute = []
            newRoute += route
            newRoute.append(cur)
            nextPath(des, newRoute) 
        

file = open("input.txt")
graph = dict()
amountRoute = 0
for line in file:
    next = line.strip("\n").split("-")
    graph.setdefault(next[0], []).append(next[1])
    graph.setdefault(next[1], []).append(next[0])
for des in graph["start"]:
    route = []
    route.append("start")
    nextPath(des, route)
print(graph)
print(amountRoute)