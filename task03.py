# Find shortest path between all nodes
shortest_paths = dict(nx.all_pairs_dijkstra_path(G))

for source in shortest_paths:
    for target in shortest_paths[source]:
        path = shortest_paths[source][target]
        length = nx.dijkstra_path_length(G, source, target)
        print(f"Shortes path between nodes {source} and {target}: {path}, length = {length}")
