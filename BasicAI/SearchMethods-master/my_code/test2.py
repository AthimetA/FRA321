import sys

from dict import cities_and_paths
from graph import Graph
stack = []
visited = []
def iterative_path(start, goal):
    root = Graph(start, start, 0, 1)
    for i in range(1,sys.maxsize):
        visited.append(root.name)
        if dfs_path(root, goal, i):
            break
        else:
            visited.pop()


def dfs_path(start, goal, depth):
    if start.name == goal:
        return True
    elif depth == 0:
        return False
    else:
        stack.append(start)
        while len(stack) != 0:
            obj = stack.pop()
            if obj.name == goal:
                print("The path is (DFS)", obj.path)
                print("The cost is (DFS)", obj.cost)
                return
            visited.append(obj.name)
            x = cities_and_paths[obj.name]
            for city, cost in x.items():
                if city in visited:
                    continue
                else:
                    node = Graph(name=city,
                                 path=obj.path + ',' + city,
                                 cost=obj.cost + cost,
                                 depth=obj.depth + 1)
                    stack.append(node)
                    dfs_path(node, goal, depth - 1)

iterative_path('Arad', 'Bucharest')