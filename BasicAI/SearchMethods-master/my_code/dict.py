import os

def cities_and_paths():
    dict_graph = {}
    path = os.path.dirname(os.path.abspath(__file__))
    dataPath = os.path.join(path, 'data.txt')
    with open(dataPath, 'r') as f:
        for line in f:
            city_a, city_b, cost = line.strip().split(' ')
            cost = int(cost)
            if city_a not in dict_graph:
                dict_graph[city_a] = {city_b: cost}
            else:
                dict_graph[city_a][city_b] = cost
            if city_b not in dict_graph:
                dict_graph[city_b] = {city_a: cost}
            else:
                dict_graph[city_b][city_a] = cost
    return dict_graph

cities_and_paths = cities_and_paths()
