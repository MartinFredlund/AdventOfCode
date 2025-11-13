def duplicate(cur, route):
    tempRoute = []
    tempRoute += route
    tempRoute.append(cur)
    for des in graph.keys():
        if tempRoute.count(des) > 1 and des.islower():
            return True
    return False


def nextPath(cur, route, has_double_visit=False):
    global amountRoute
    for des in graph[cur]:
        if has_double_visit == False:
            has_double_visit = duplicate(cur, route)
        if des == "end":
            amountRoute += 1
        elif des == "start":
            pass
        elif not (has_double_visit) or not (des in route) or des.isupper():
            newRoute = []
            newRoute += route
            newRoute.append(cur)
            nextPath(des, newRoute, has_double_visit)


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

print(amountRoute)
