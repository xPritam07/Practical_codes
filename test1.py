def bully_algorith(process, initiator):
    print(f"Process {initiator} starts the election.")

    for p in sorted(process, reverse=True):
        if p > initiator:
            print(f"Process {p} responds to election.")
            return bully_algorith(process, p)
        
    print(f"Process {initiator} becomes the coordinator")
    return initiator

processes = [1,2,3,4,5]
coordinator = bully_algorith(process=processes, initiator=2)
print(f"{coordinator} is the new coordinator")