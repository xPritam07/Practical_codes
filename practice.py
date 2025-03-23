import heapq
goal_state ='Goal'

def transition(state):
    transition={
        'A':[['B',1],['C',3]],
        'B':[('D',2),('E',4)],
        'C':[('F',3),('G',5)],
        'D':['Goal',3],
        'E':['Goal',4],
        'F':['Goal',3],
        'G':['Goal',5]
    }
    return transition.get(state,[])
def heuristic(state):
    heuristic_values={
        'A':6,
        'B':5,
        'C':7,
        'D':3,
        'E':4,
        'F':3,
        'G':5,
        'Goal':0
    }
    return heuristic_values.get(state,float('inf'))
def astar(start_state):
    frontier=[(heuristic(start_state),0,start_state)]
    heapq.heapify(frontier)
    explored=set()

    while frontier:
        _,cost,current_state=heapq.heappop(frontier)
        if current_state==goal_state:
            return True 
        if current_state not in explored:
            explored.add(current_state)

            for neighbor, action_cost in transition(current_state):
                heapq.heappush(frontier,(cost+action_cost+heuristic(neighbor), cost+action_cost, neighbor))

    return False