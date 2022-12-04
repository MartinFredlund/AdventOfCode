def duplicate(cur, route):
    tempRoute = []
    tempRoute += route
    tempRoute.append(cur)
    for des in graph.keys():
        if(tempRoute.count(des) > 1 and des.islower()):
        #print("2 or more", des, route)
            return True
    return False

def nextPath(cur, route):
    global amountRoute
    for des in graph[cur]:
        #print("Cur:", cur, "Des:", des, "route: ", route, "dup", not (duplicate(cur, route)), "des in route: ", not (des in route), "upper:", des.isupper(), "if:", (not (duplicate(cur, route)) or not (des in route) or des.isupper()))
        if(des == "end"):
            amountRoute += 1
            endRoute = []
            endRoute += route
            endRoute.append(cur)
            endRoute.append("end")
            #print("End", endRoute)
        elif(des == "start"):
            amountRoute += 0
        elif(not (duplicate(cur, route)) or not (des in route) or des.isupper()):
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