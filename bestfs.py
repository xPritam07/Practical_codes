import heapq

def best_first_search(graph, start, goal, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))  # Push (heuristic, node)
    visited = set()

    while priority_queue:
        _, node = heapq.heappop(priority_queue)  # Pop the node with the lowest heuristic

        print(node, end=" ")

        if node == goal:
            print("\nGoal Found!")
            return True

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))

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

# Define heuristic values for each node (Example values, usually based on some estimate)
heuristic = {
    "A": 6,
    "B": 4,
    "C": 5,
    "D": 3,
    "E": 2,
    "F": 4,
    "G": 3,
    "H": 1  # Goal node should have the lowest heuristic value
}

# Call the Best-First Search
best_first_search(graph, "A", "H", heuristic)
