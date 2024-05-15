# Find shortest path between all nodes
def dijkstra_algorithm(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    not_visited = list(graph.nodes)

    while not_visited:
        current_vertex = min(not_visited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight["weight"]

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        not_visited.remove(current_vertex)

    return distances

for start in G.nodes:
    shortest_paths = dijkstra_algorithm(G, start)
    print(f"Shortes path from nodes {start}: {shortest_paths}")  

#Shortes path from nodes Alice: {'Alice': 0, 'Bob': 4, 'Charlie': 2, 'David': 5, 'Eve': 5}
#Shortes path from nodes Bob: {'Alice': inf, 'Bob': 0, 'Charlie': 17, 'David': 10, 'Eve': 16}
#Shortes path from nodes Charlie: {'Alice': inf, 'Bob': inf, 'Charlie': 0, 'David': inf, 'Eve': 3}
#Shortes path from nodes David: {'Alice': inf, 'Bob': inf, 'Charlie': 7, 'David': 0, 'Eve': 6}
#Shortes path from nodes Eve: {'Alice': inf, 'Bob': inf, 'Charlie': inf, 'David': inf, 'Eve': 0}
