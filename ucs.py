import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = []  # Min-heap (priority queue)
    heapq.heappush(priority_queue, (0, start))  # (cost, node)
    visited = set()
    parent = {start: None}  # To track the path
    cost_so_far = {start: 0}  # Cost to reach each node

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)  # Get the least-cost node

        print(node, end=" ")

        if node == goal:
            print("\nGoal Found!")
            # Reconstruct the path
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            print("Path:", " -> ".join(reversed(path)))
            print("Total Cost:", cost)
            return True

        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph.get(node, []):
                new_cost = cost + edge_cost
                if neighbor not in visited or new_cost < cost_so_far.get(neighbor, float('inf')):
                    cost_so_far[neighbor] = new_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor))
                    parent[neighbor] = node  # Store parent for path reconstruction

    print("\nGoal not found")
    return False

# Define the graph with weighted edges
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("F", 1), ("G", 3)],
    "D": [],
    "E": [("H", 2)],
    "F": [],
    "G": [],
    "H": []
}

# Call UCS function
uniform_cost_search(graph, "A", "H")
