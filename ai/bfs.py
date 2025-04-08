from collections import deque

def breadth_first_search(graph, start, goal):
    queue = deque([start])  # Initialize queue with the start node
    visited = set()         # Keep track of visited nodes
    parent = {start: None}  # To reconstruct the path

    while queue:
        node = queue.popleft()  # Dequeue a node
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
            for neighbor in graph.get(node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
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

# Call the BFS function
breadth_first_search(graph, "A", "H")
