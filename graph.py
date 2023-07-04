from queue import Queue
from queue import LifoQueue


class Graph:
    def __init__(self, graph_dict=None, graph_dict_without_edge=None):
        self.graph_dict = graph_dict or {}
        self.graph_dict_without_edge = graph_dict_without_edge or {}
        self.ids_visited_path = []

    def connect(self, item_key, key, item_value):
        self.graph_dict.setdefault(item_key, {})[key] = item_value

    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

    def bfs(self, start, end):
        visited = {}
        distance = {}
        parent = {}
        queue = Queue()

        for city in self.graph_dict_without_edge.keys():
            visited[city] = False
            parent[city] = None
            distance[city] = -1

        starting_city = start
        visited[starting_city] = True
        distance[starting_city] = 0
        queue.put(starting_city)

        while not queue.empty():
            u = queue.get()
            for v in self.graph_dict_without_edge[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    distance[v] = distance[u] + 1
                    queue.put(v)

        destination = end
        path = []
        while destination is not None:
            path.append(destination)
            destination = parent[destination]

        path.reverse()

        print(f'Starting to destination path: {path}')
        print(f'All visited paths: {visited.keys()}')
        print(f'Total path cost: {len(path) - 1}')

    def ids(self, start, target):
        depth = 1
        bottom_reached = False
        while not bottom_reached:
            result, bottom_reached = self.ids_rec(start, target, 0, depth)
            if result is not None:
                return result
            depth += 1
        return None

    def ids_rec(self, start2, target, current_depth, max_depth):
        self.ids_visited_path.append(start2)
        if start2 == target:
            return start2, True
        if current_depth == max_depth:
            if not self.graph_dict_without_edge.get(start2):
                return None, False
            else:
                return None, True
        bottom_reached = False
        for i in self.graph_dict_without_edge[start2]:
            result, bottom_reached_rec = self.ids_rec(i, target,
                                                      current_depth + 1,
                                                      max_depth)
            if result is not None:
                return result, True
            bottom_reached = bottom_reached and bottom_reached_rec
        return None, bottom_reached

    def dfs_paths(self, start, goal):
        visited = {}
        distance = {}
        parent = {}
        dfs_traversal_output = []
        stack = LifoQueue()
        for city in self.graph_dict_without_edge.keys():
            visited[city] = False
            parent[city] = None
            distance[city] = -1
        starting_city = start
        distance[starting_city] = 0
        stack.put(start)

        while not stack.empty():
            obj = stack.get()
            if not visited[obj]:
                visited[obj] = True
                if obj == goal:
                    dfs_traversal_output.append(obj)
                    print(f'Starting to destination path: {dfs_traversal_output}')
                    print(f'All visited paths: {visited.keys()}')
                    print(f'Total path cost: {len(dfs_traversal_output) - 1}')
                    return
                else:
                    dfs_traversal_output.append(obj)
                    for v in self.graph_dict_without_edge[obj]:
                        parent[v] = obj
                        distance[v] = distance[obj] + 1
                        stack.put(v)
