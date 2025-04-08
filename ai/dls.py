def dls(graph, start, goal, depth_limit):
    stack = [(start, 0)]
    while stack:
        node, depth = stack.pop()

        print("Visiting : ", node, end='\n')

        if node == goal:
            print("Goal Found!")
            return True
        
        if depth < depth_limit:
            for neighbour in reversed(graph.get(node,[])):
                stack.append((neighbour, depth+1))

    print("\nGoal not found!")

graph = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["F","G"],
    "D":[],
    "E":["H"],
    "F":[],
    "G":[],
    "H":[]
}

dls(graph,"A", "H", 3)