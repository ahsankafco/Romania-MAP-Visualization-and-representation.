import networkx
import matplotlib.pyplot as plt
from graph import Graph
from map_data import romania_locations, romania_map, romania_map_without_edge


class GraphicalMapGui:
    def __init__(self, geo_locations, geo_map):
        self.geo_locations = geo_locations
        self.geo_map = geo_map
        self.graph_network = networkx.Graph()
        self.node_labels = dict()
        self.edge_labels = dict()

    def structure_graph(self):
        for n, p in self.geo_locations.items():
            self.graph_network.add_node(n)
            self.node_labels[n] = n

        return {k: [v[0], v[1] - 10] for k, v in self.geo_locations.items()}

    def connect_nodes(self):
        for node in self.geo_map.nodes():
            connections = self.geo_map.get(node)
            for connection in connections.keys():
                distance = connections[connection]
                self.graph_network.add_edge(node, connection)
                self.edge_labels[(node, connection)] = distance

    def draw_network(self):
        networkx.draw(
            self.graph_network,
            pos=self.geo_locations,
            node_color='red'
        )

    def draw_node_labels(self, node_label_pos):
        node_label_handles = networkx.draw_networkx_labels(
            self.graph_network,
            pos=node_label_pos,
            labels=self.node_labels,
            font_size=8)

        [label.set_bbox(dict(facecolor='white', edgecolor='red'))
         for label in node_label_handles.values()]

    def draw_edge_labels(self):
        networkx.draw_networkx_edge_labels(
            self.graph_network,
            pos=self.geo_locations,
            edge_labels=self.edge_labels,
            font_size=10)

    def show_map(self):
        plt.figure(figsize=(13, 10))
        self.connect_nodes()
        self.draw_network()
        self.draw_node_labels(self.structure_graph())
        self.draw_edge_labels()
        plt.show()


def app():
    continue_program = True
    while continue_program:
        romania_map_graph = Graph(romania_map, romania_map_without_edge)
        romania_map_gui = GraphicalMapGui(romania_locations, romania_map_graph)
        print("Welcome to Romania MAP Representation")
        print("Please select from below options")
        print("|1|.Represent the romania map in GUI")
        print("|2|.Search in Romania Map")

        option = int(input(""))
        show_map = 1
        search_map = 2
        bfs = 1
        dfs = 2
        ids = 3

        Arad = 1
        Zerind = 2
        Oradea = 3
        Sibiu = 4
        Timisoara = 5
        Lugoj = 6
        Mehadia = 7
        Drobeta = 8
        Craiova = 9
        Rimnicu = 10
        Fagaras = 11
        Pitesti = 12
        Giurgiu = 13
        Urziceni = 14
        Hirsova = 15
        Eforie = 16
        Vaslui = 17
        Iasi = 18
        Neamt = 19

        if option == show_map:
            romania_map_gui.show_map()
        if option == search_map:
            print("Please select the search Algorithm ")
            search_option = int(input("1. BFS | 2. DFS | 3. IDS "))
            if search_option == bfs:

                print("Please select the Start City: ")
                print("|1|. Arad |2|. Zerind |3|. Oradea |4|. Sibiu |5|. Timisoara")
                print("|6|. Lugoj |7|. Mehadia |8|. Drobeta |9|. Craiova |10|. Rimnicu")
                print("|11|. Fagaras |12|. Pitesti |13|. Giurgiu |14|. Urziceni |15|. Hirsova")
                print("|16|. Eforie |17|. Vaslui |18|. Iasi  |19|. Neamt")
                bfs_option = int(input())
                if bfs_option == Arad:
                    romania_map_graph.bfs('Arad', 'Bucharest')
                elif bfs_option == Zerind:
                    romania_map_graph.bfs('Zerind', 'Bucharest')
                elif bfs_option == Oradea:
                    romania_map_graph.bfs('Oradea', 'Bucharest')
                elif bfs_option == Sibiu:
                    romania_map_graph.bfs('Sibiu', 'Bucharest')
                elif bfs_option == Timisoara:
                    romania_map_graph.bfs('Timisoara', 'Bucharest')
                elif bfs_option == Lugoj:
                    romania_map_graph.bfs('Lugoj', 'Bucharest')
                elif bfs_option == Mehadia:
                    romania_map_graph.bfs('Mehadia', 'Bucharest')
                elif bfs_option == Drobeta:
                    romania_map_graph.bfs('Drobeta', 'Bucharest')
                elif bfs_option == Craiova:
                    romania_map_graph.bfs('Craiova', 'Bucharest')
                elif bfs_option == Rimnicu:
                    romania_map_graph.bfs('Rimnicu', 'Bucharest')
                elif bfs_option == Fagaras:
                    romania_map_graph.bfs('Fagaras', 'Bucharest')
                elif bfs_option == Pitesti:
                    romania_map_graph.bfs('Pitesti', 'Bucharest')
                elif bfs_option == Giurgiu:
                    romania_map_graph.bfs('Giurgiu', 'Bucharest')
                elif bfs_option == Urziceni:
                    romania_map_graph.bfs('Urziceni', 'Bucharest')
                elif bfs_option == Hirsova:
                    romania_map_graph.bfs('Hirsova', 'Bucharest')
                elif bfs_option == Eforie:
                    romania_map_graph.bfs('Eforie', 'Bucharest')
                elif bfs_option == Vaslui:
                    romania_map_graph.bfs('Vaslui', 'Bucharest')
                elif bfs_option == Iasi:
                    romania_map_graph.bfs('Iasi', 'Bucharest')
                elif bfs_option == Neamt:
                    romania_map_graph.bfs('Neamt', 'Bucharest')


            if search_option == dfs:
                print("Please select the Start City: ")
                print("|1|. Arad |2|. Zerind |3|. Oradea |4|. Sibiu |5|. Timisoara")
                print("|6|. Lugoj |7|. Mehadia |8|. Drobeta |9|. Craiova |10|. Rimnicu")
                print("|11|. Fagaras |12|. Pitesti |13|. Giurgiu |14|. Urziceni |15|. Hirsova")
                print("|16|. Eforie |17|. Vaslui |18|. Iasi  |19|. Neamt")
                dfs_option = int(input())
                if dfs_option == Arad:
                    romania_map_graph.dfs_paths('Arad', 'Bucharest')
                elif dfs_option == Zerind:
                    romania_map_graph.dfs_paths('Zerind', 'Bucharest')
                elif dfs_option == Oradea:
                    romania_map_graph.dfs_paths('Oradea', 'Bucharest')
                elif dfs_option == Sibiu:
                    romania_map_graph.dfs_paths('Sibiu', 'Bucharest')
                elif dfs_option == Timisoara:
                    romania_map_graph.dfs_paths('Timisoara', 'Bucharest')
                elif dfs_option == Lugoj:
                    romania_map_graph.dfs_paths('Lugoj', 'Bucharest')
                elif dfs_option == Mehadia:
                    romania_map_graph.dfs_paths('Mehadia', 'Bucharest')
                elif dfs_option == Drobeta:
                    romania_map_graph.dfs_paths('Drobeta', 'Bucharest')
                elif dfs_option == Craiova:
                    romania_map_graph.dfs_paths('Craiova', 'Bucharest')
                elif dfs_option == Rimnicu:
                    romania_map_graph.dfs_paths('Rimnicu', 'Bucharest')
                elif dfs_option == Fagaras:
                    romania_map_graph.dfs_paths('Fagaras', 'Bucharest')
                elif dfs_option == Pitesti:
                    romania_map_graph.dfs_paths('Pitesti', 'Bucharest')
                elif dfs_option == Giurgiu:
                    romania_map_graph.dfs_paths('Giurgiu', 'Bucharest')
                elif dfs_option == Urziceni:
                    romania_map_graph.dfs_paths('Urziceni', 'Bucharest')
                elif dfs_option == Hirsova:
                    romania_map_graph.dfs_paths('Hirsova', 'Bucharest')
                elif dfs_option == Eforie:
                    romania_map_graph.dfs_paths('Eforie', 'Bucharest')
                elif dfs_option == Vaslui:
                    romania_map_graph.dfs_paths('Vaslui', 'Bucharest')
                elif dfs_option == Iasi:
                    romania_map_graph.dfs_paths('Iasi', 'Bucharest')
                elif dfs_option == Neamt:
                    romania_map_graph.dfs_paths('Neamt', 'Bucharest')

            if search_option == ids:
                print("Please select the Start City: ")
                print("|1|. Arad |2|. Zerind |3|. Oradea |4|. Sibiu |5|. Timisoara")
                print("|6|. Lugoj |7|. Mehadia |8|. Drobeta |9|. Craiova |10|. Rimnicu")
                print("|11|. Fagaras |12|. Pitesti |13|. Giurgiu |14|. Urziceni |15|. Hirsova")
                print("|16|. Eforie |17|. Vaslui |18|. Iasi  |19|. Neamt")
                ids_option = int(input())
                if ids_option == Arad:
                    romania_map_graph.ids('Arad', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")

                if ids_option == Zerind:
                    romania_map_graph.ids('Zerind', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Oradea:
                    romania_map_graph.ids('Oradea', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Sibiu:
                    romania_map_graph.ids('Sibiu', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Timisoara:
                    romania_map_graph.ids('Timisoara', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Lugoj:
                    romania_map_graph.ids('Lugoj', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Mehadia:
                    romania_map_graph.ids('Mehadia', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Drobeta:
                    romania_map_graph.ids('Drobeta', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Craiova:
                    romania_map_graph.ids('Craiova', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Rimnicu:
                    romania_map_graph.ids('Rimnicu', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Fagaras:
                    romania_map_graph.ids('Fagaras', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Pitesti:
                    romania_map_graph.ids('Pitesti', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Giurgiu:
                    romania_map_graph.ids('Giurgiu', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Urziceni:
                    romania_map_graph.ids('Urziceni', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Hirsova:
                    romania_map_graph.ids('Hirsova', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Eforie:
                    romania_map_graph.ids('Eforie', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Vaslui:
                    romania_map_graph.ids('Vaslui', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Iasi:
                    romania_map_graph.ids('Iasi', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")
                if ids_option == Neamt:
                    romania_map_graph.ids('Neamt', 'Bucharest')
                    res = []
                    for t in romania_map_graph.ids_visited_path:
                        if t not in res:
                            res.append(t)
                    print("Starting to destination path: " + str(res))
                    print(f"visited path: {romania_map_graph.ids_visited_path}")
                    print(f"Total path cost: {len(res) - 1}")



        print("Do you want to continue?")
        user_continue_state = str(input())
        continue_program = user_continue_state == "y" or user_continue_state == "Y"
    print("Thank You for Using this app")
if __name__ == "__main__":
    try:
        app()
    except KeyboardInterrupt:
        print("Program was forcefully ended")
