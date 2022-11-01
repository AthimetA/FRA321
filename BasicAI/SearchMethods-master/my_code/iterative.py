from dict import cities_and_paths
path = []
def iterative_path(start, goal):
    depth = 0
    while(True):
        result = DLS(start, goal, depth)
        if (result == goal):
            print(path)
        depth = depth + 1

def DLS(node, goal, depth):
    if (depth == 0 and node == goal):
        return node
    elif (depth > 0):
        for child in cities_and_paths[node]:
            path.append(node)
            print(path)
            DLS(child, goal, depth-1)
    else:
        return

iterative_path('Arad','Bucharest')