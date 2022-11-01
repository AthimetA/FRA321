import queue

from dict import cities_and_paths
from graph import Graph


def iterative(start, goal):
    root = Graph(start, start, 0, 1)
    stack = []
    visited = []
#    q = queue.Queue()
    stack.append(root)
#     if obj.depth > 3:
#         q.put(root)
#         while not q.empty():
#             obj = q.get()
#             if obj.name == goal:
#                 print("\nThe path is", obj.path)
#                 print("\nThe cost is", obj.cost)
#                 return
#             visited.append(obj)
#             x = cities_and_paths[obj.name]
#             for city, cost in x.items():
#                 if city in visited:
#                     continue
#                 else:
#                     node = Graph(name=city,
#                                  path=obj.path + ',' + city,
#                                  cost=obj.cost + cost,
#                                  depth=obj.depth + 1)
#                     q.put(node)
#     else:
#         while len(stack) != 0:
#             obj = stack.pop()
#             if obj.name == goal:
#                 print("The path is", obj.path)
#                 print("The cost is", obj.cost)
#                 print("The depth is", obj.depth)
#                 return
#             visited.append(obj.name)
#             x = cities_and_paths[obj.name]
#             for city, cost in x.items():
#                 if city in visited:
#                     continue
#                 else:
#                     node = Graph(name=city,
#                                  path=obj.path + ',' + city,
#                                  cost=obj.cost + cost,
#                                  depth=obj.depth + 1)
#                     stack.append(node)
#
#
# iterative('Arad', 'Bucharest')
