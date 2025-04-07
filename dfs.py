def depth_first_search(graph, start, goal):
    stack = [start]  # Initialize stack with the start node
    visited = set()  # Keep track of visited nodes
    parent = {start: None}  # To reconstruct the path

    while stack:
        node = stack.pop()  # Pop the last added node (LIFO)
        print(node, end=" ")

        if node == goal:
            print("\nGoal Found!")
            # Reconstruct the path
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            print("Path:", " -> ".join(reversed(path)))
            return True

        if node not in visited:
            visited.add(node)
            for neighbor in reversed(graph.get(node, [])):  # Reverse to maintain expected order
                if neighbor not in visited:
                    stack.append(neighbor)
                    parent[neighbor] = node  # Store parent for path reconstruction

    print("\nGoal not found")
    return False

# Define the graph as an adjacency list
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": ["H"],
    "F": [],
    "G": [],
    "H": []
}

# Call the DFS function
depth_first_search(graph, "A", "H")
