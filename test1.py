def bankers_algorithm(allocation, max_demand, available):
    need = [[max_demand[i][j] for j in range(len(available))] for i in range(len(allocation))]
    finished = [False]*len(allocation)
    safe_seq = []
    if len(safe_seq)<len(allocation):
        allocated = False
        for i in range(len(allocation)):
            if not finished[i] and all(need[i][j] <= available[j] for j in range(len(available))):
                for j in range(len(available)):
                    available[j] += allocation[i][j]

                finished[i] = True
                safe_seq.append(i)