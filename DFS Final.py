from queue import Queue

romaniaMap = {
    'Arad': ['Sibiu', 'Zerind', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Iasi', 'Urziceni'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}
def dfs(start, goal):
    visited = {}
    distance = {}
    parent = {}
    dfs_traversal_output = []
    stack = []

    for city in romaniaMap.keys():
        visited[city] = False
        parent[city] = None
        distance[city] = -1

    startingCity = start
    visited[startingCity] = True
    distance[startingCity] = 0
    stack.append(startingCity)

    while len(stack) != 0:
        obj = stack.pop()
        dfs_traversal_output.append(obj)

        for v in romaniaMap[obj]:
            if not visited[v]:
                visited[v] = True
                parent[v] = obj
                distance[v] = distance[obj] + 1

    g = goal
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]

    path.reverse()
    print(path)

dfs('Arad', 'Bucharest')



