#Forward_chaining

global_facts=[['plant','mango'], ['eating', 'mango'],['seed', 'sprouts']]
global_is_changed=True

def assert_fact(fact):
    global global_facts
    global global_is_changed
    if fact not in global_facts:
        global_facts.append(fact)
        global_is_changed=True

while global_is_changed:
    global_is_changed= False
    for x in global_facts:
        if x[0]=='seed':
            assert_fact(['plant',x[0]])
        if x[0]=='plant':
            assert_fact(['fruit',x[0]])

        if x[0]=='fruit' and ['eating',x[0]] in global_facts:
            assert_fact(['eating',x[0]])

print(global_facts)

#Backward Chaining


global_facts=[['vertebrate','duck'],['flying', 'duck'],['mammal', 'cat']]

def is_fact_known(fact):
    return fact in global_facts

def backward_chain(goal):
    if is_fact_known(goal):
        return True
    
    entity = goal[1]

    if goal[0]=='vertebrate':
        if backward_chain(['mammal',entity]):
            return True
    
    if goal[0]=='animal':
        if backward_chain(['vertebrate', entity]):
            return True
        
    if goal[0]=='bird':
        if backward_chain(['vertebrate', entity]) and backward_chain(['flying', entity]):
            return True

query1=backward_chain(['bird', 'duck'])
query2=backward_chain(['animal', 'cat'])

print(query1)
print(query2)