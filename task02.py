#BFS
def find_all_paths_using_breadth_first_search(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths_using_breadth_first_search(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

# Find all path between nodes "Alice" and "Bob"
all_paths = find_all_paths_using_breadth_first_search(dict(G.adjacency()), "Alice", "Charlie")
print("All paths between nodes Alice and Charlie using BFS:")
for path in all_paths:
    print(path)


#DFS
def find_all_paths__using_depth_first_search(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths__using_depth_first_search(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

# Find all path between nodes "Alice" and "Bob"
all_paths_dfs = find_all_paths__using_depth_first_search(dict(G.adjacency()), "Alice", "Charlie")
print("All paths between nodes Alice and Charlie using DFS:")
for path in all_paths_dfs:
    print(path)
