#BFS
def find_all_paths_using_breadth_first_search(graph, start, end):
    queue = [(start, [start])]
    paths = []
    while queue:
        current, path = queue.pop(0)
        for neighbor in graph.neighbors(current):
            if neighbor not in path:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
                if neighbor == end:
                    paths.append(new_path)
    return paths

# Find all path between nodes "Alice" and "Bob"
all_paths = find_all_paths_using_breadth_first_search(G, "Alice", "Charlie")
print("All paths between nodes Alice and Charlie using BFS:")
for path in all_paths:
    print(path)

#All paths between nodes Alice and Charlie using BFS:
#['Alice', 'Charlie']
#['Alice', 'David', 'Charlie']
#['Alice', 'Bob', 'David', 'Charlie']


#DFS
def find_all_paths__using_depth_first_search(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for neighbor in graph.neighbors(start):
          if neighbor not in path:
              new_paths = find_all_paths__using_depth_first_search(graph, neighbor, end, path)
              for p in new_paths:
                  paths.append(p)
    return paths

# Find all path between nodes "Alice" and "Bob"
all_paths_dfs = find_all_paths__using_depth_first_search(G, "Alice", "Charlie")
print("All paths between nodes Alice and Charlie using DFS:")
for path in all_paths_dfs:
    print(path)

#All paths between nodes Alice and Charlie using DFS:
#['Alice', 'Bob', 'David', 'Charlie']
#['Alice', 'Charlie']
#['Alice', 'David', 'Charlie']
